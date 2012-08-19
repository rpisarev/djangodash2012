from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, render_to_response, HttpResponseRedirect
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F,Q
from django.conf import settings
from itertools import chain
import json
import datetime
import random

from core.models import Image,Vote,Miracle,Year
from .utils import get_client_ip, set_cookie


def random_miracle(request):
    miracle = Miracle.objects.order_by('?')[0]
    return HttpResponseRedirect(miracle.get_absolute_url())

def about(request, template='about.html'):
    return render(request, template)

def rating(request, template='rating.html'):
    images = Image.objects.all().order_by("-rating")[:24]
    context = {
    'images':images,
    }
    return render(request, template,context)

def main(request, template='main.html'):
    miracles = Miracle.objects.order_by('?').all()
    context = ({'miracles':miracles})
    return render(request, template, context)

def get_images(request,miracle_slug,initial,year='today'):
    service_types = ('google',)
    if year == 'today':
        year = None
    try:
        year = Year.objects.get(value=year)
    except ObjectDoesNotExist:
        service_types = ('flickr','instagram')
    big_image_alias = Image.IMAGE_SIZES[1][0]
    small_image_alias = Image.IMAGE_SIZES[0][0]
    session_key = 'viewed_images_%s' % miracle_slug

    if int(initial) == 1:
        big_images_num = 3
        small_images_num = 12
        viewed_images = []        
    else:
        viewed_images = request.session.get(session_key,[])
        big_images_num = random.randint(1,2)
        small_images_num = 0

    big_images = Image.objects.filter(Q(type__in=service_types)\
        &Q(year=year)& Q(miracle__slug=miracle_slug)&
        Q(size=big_image_alias)&~Q(id__in=viewed_images))\
        .values('id','url','size','title','rating').order_by('?')[:big_images_num]

    small_images_count = small_images_num+4*(3-len(big_images))
    small_images = Image.objects.filter(Q(type__in=service_types)\
        &Q(year=year)&Q(miracle__slug=miracle_slug)&
        Q(size=small_image_alias)&~Q(id__in=viewed_images)).\
        values('id','url','size','title','rating').order_by('?')[:small_images_count]
    
    images = list(chain(big_images, small_images))
    if len(images)==0:
        return HttpResponse()
    image_ids = map(lambda x:x.get('id'),images)
    viewed_images.reverse()
    viewed_images = viewed_images[len(image_ids):]+image_ids
    request.session[session_key]=viewed_images

    return HttpResponse(json.dumps(tuple(images)))


def miracle(request, miracle_slug, template='miracle.html'):
    miracle = get_object_or_404(Miracle, slug = miracle_slug)
    years = Year.objects.order_by('-value').all()
    context = Context({'miracle':miracle, 'years':years})
    response = render_to_response(template, context_instance=context)
    cookie_key = "miracle_%s" % miracle_slug
    days_expire = 1
    if not request.COOKIES.get(cookie_key):
        set_cookie(response,cookie_key,True,days_expire)
        Miracle.objects.filter(slug=miracle_slug).update(views_count=F('views_count')+1)

    return response

def vote(request,image_id,value):
    cookie_key = "image_%s"%image_id
    days_expire = 1
    if request.is_ajax and not request.COOKIES.get(cookie_key):
        try:
            user_ip = get_client_ip(request)
            time_ago = datetime.datetime.now()-datetime.timedelta(days=days_expire)
            Vote.objects.get(user_ip=user_ip,created__gt=time_ago,image_id=image_id)
        except ObjectDoesNotExist:
                response = HttpResponse()
                try:
                    image = Image.objects.get(pk=image_id)
                except ObjectDoesNotExist:
                    return response
                vote = Vote()
                vote.value = 1 if value=='up' else -1
                vote.user_ip = user_ip
                vote.image = image
                vote.created = datetime.datetime.now()
                vote.save()
                image.rating = Vote.objects.filter(image=image)\
                    .aggregate(sum=Sum('value')).get('sum')
                image.save()
                recalc_sizes(image.miracle)
                image =Image.objects.get(id=image.pk)
                new_data = {'rating':image.rating,'id':image.pk,'size':image.size}
                new_data_encoded = json.dumps(new_data)
                response.write(new_data_encoded)
                set_cookie(response,cookie_key,True,days_expire)
                return response
    return HttpResponse()


def recalc_sizes(miracle):
    images_count = Image.objects.filter(miracle=miracle).count()
    big_image_alias = Image.IMAGE_SIZES[1][0]
    small_image_alias = Image.IMAGE_SIZES[0][0]
    big_image_num = int(images_count*settings.BIG_IMAGES_RATIO)

    images_to_big= Image.objects.filter(miracle=miracle).order_by('-rating')\
        .values('id')[:big_image_num]
    sql_in = [Q(id=i) for i in images_to_big]
    Image.objects.filter(featured=True,*sql_in).update(size=big_image_alias)

    images_to_small = Image.objects.filter(miracle=miracle).order_by('-rating')\
        .values('id')[big_image_num:]

    sql_in = [Q(id=i) for i in images_to_small]    
    Image.objects.filter(featured=True,*sql_in).update(size=small_image_alias)

    return
