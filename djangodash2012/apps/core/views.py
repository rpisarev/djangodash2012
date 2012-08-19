from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, RequestContext,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
import datetime

from core.models import Image,Vote,Miracle

def main(request, template='main.html'):
    miracles = Miracle.objects.all()
    context = ({'miracles':miracles})
    return render(request, template, context)

def miracle(request, miracle_slug, template='miracle.html'):
    miracle = get_object_or_404(Miracle, slug = miracle_slug)
    context = ({'miracle':miracle})
    return render(request, template, context)

def miracle_year(request, miracle_slug, year):
    return HttpResponse()

def vote(request,image_id,value):
    if request.is_ajax():
        try:
            user_ip = get_client_ip(request)
            month_ago = datetime.datetime.now()-datetime.timedelta(weeks=4)
            Vote.objects.get(user_ip=user_ip,created__gt=month_ago)
        except :
                try:
                    image = Image.objects.get(pk=image_id)
                except ObjectDoesNotExist:
                    return HttpResponse()
                vote = Vote()
                vote.value = 1 if value=='up' else -1
                vote.user_ip = user_ip
                vote.image=image
                vote.created = datetime.datetime.now()
                vote.save()

                image.rating = Vote.objects.filter(image=image)\
                    .aggregate(sum=Sum('value')).get('sum')
                image.save()
                return HttpResponse(image.rating)
    return HttpResponse()
