from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, render_to_response, HttpResponseRedirect
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F
import datetime
from django.conf import settings


from core.models import Image,Vote,Miracle

from .utils import get_client_ip, set_cookie


def random(request):
    miracle = Miracle.objects.order_by('?')[0]
    return HttpResponseRedirect(miracle.get_absolute_url())

def about(request, template='about.html'):
    return render(request, template)

def rating(request, template='rating.html'):
    # rating
    return render(request, template)

def main(request, template='main.html'):
    miracles = Miracle.objects.all()
    context = ({'miracles':miracles})
    return render(request, template, context)

def miracle(request, miracle_slug, template='miracle.html'):
    miracle = get_object_or_404(Miracle, slug = miracle_slug)
    context = Context({'miracle':miracle})
    response = render_to_response(template, context_instance=context)
    cookie_key = "miracle_%s" % miracle_slug
    days_expire = 1
    if not request.COOKIES.get(cookie_key):
        set_cookie(response,cookie_key,True,days_expire)
        Miracle.objects.filter(slug=miracle_slug).update(views_count=F('views_count')+1)

    return response

def miracle_year(request, miracle_slug, year):
    return HttpResponse()

def vote(request,image_id,value):
    import pdb
    pdb.set_trace()
    cookie_key = "image_%s"%image_id
    days_expire = 1
    if request.is_ajax() and not request.COOKIES.get(cookie_key):
        try:
            user_ip = get_client_ip(request)
            time_ago = datetime.datetime.now()-datetime.timedelta(days=days_expire)
            Vote.objects.get(user_ip=user_ip,created__gt=time_ago,image_id=image_id)

        except :
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
                response.write(image.rating)
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
    Image.objects.filter(id__in=images_to_big).update(size=big_image_alias)

    images_to_small = Image.objects.filter(miracle=miracle).order_by('-rating')\
        .values('id')[big_image_num:]
    Image.objects.filter(id__in=images_to_small).update(size=small_image_alias)

    return
