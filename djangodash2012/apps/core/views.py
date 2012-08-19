from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F
import datetime

from core.models import Image,Vote,Miracle

from .utils import get_client_ip, set_cookie


def main(request, template='main.html'):
    miracles = Miracle.objects.all()
    context = ({'miracles':miracles})
    return render(request, template, context)

def miracle(request, miracle_slug, template='miracle.html'):
    miracle = get_object_or_404(Miracle, slug = miracle_slug)
    context = ({'miracle':miracle})
    response = render_to_response(template, context=context)
    cookie_key = "miracle_%s" % miracle_slug
    days_expire = 1
    if not request.COOKIES.get(cookie_key):
        set_cookie(response,key,value,days_expire)
        Miracle.objects.filter(slug=miracle_slug).update(views_count=F('views')+1)

    return render(request, template, context)

def miracle_year(request, miracle_slug, year):
    return HttpResponse()

def vote(request,image_id,value):
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
