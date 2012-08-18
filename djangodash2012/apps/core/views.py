from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, RequestContext,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
import datetime

from core.models import Image,Vote,Object
from .utils import get_client_ip

def main(request,template='main.html'):
    context = ({})
    return render(request, template, context)

def object(request,obj_slug,template='object.html'):
    obj = get_object_or_404(Object,slug = obj_slug)
    context = ({'obj':obj})
    return render(request, template, context)

def object_year(request,obj_slug,year):
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


def test_google(request):
    return HttpResponse('LOL')

def test_instagram(request):
    return HttpResponse()

def test_flickr(request,template='main.html'):
    import flickrapi
    imgs = []
    api_key = '333ecc67971ffa129d1e24f56eb45a3a'
    flickr = flickrapi.FlickrAPI(api_key)
    photos = flickr.walk(tag_mode='all',
        tags='Eifel Tower',
        min_taken_date='2011-08-20',
        max_taken_date='2012-08-26')
    for photo in photos:
        secret = photo.get('secret')
        server = photo.get('server')
        id = photo.get('id')
        farm = photo.get('farm')
        size='z'
        url = r"""http://farm%s.staticflickr.com/%s/%s_%s_%s.jpg""" % (farm,server,id,secret,size)
        imgs.append(url)
    context = {'images':imgs}
    return render(request, template, context)