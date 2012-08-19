from django.shortcuts import HttpResponse
from core.models import Year,Image,Miracle
from django.conf import settings
from django.db import IntegrityError

import flickrapi
import time
import urllib2,urllib
import simplejson

def parse_flickr(request):
    miracles = Miracle.objects.all()
    years = Year.objects.all()
    for miracle in miracles:
        for year in years:
            api_key = '333ecc67971ffa129d1e24f56eb45a3a'
            flickr = flickrapi.FlickrAPI(api_key)
            photos = flickr.walk(tag_mode='all',
                tags=miracle.flickr_tags,
                min_taken_date='%s-01-01' % year,
                max_taken_date='$s-12-31' % year,
#                sort = 'interestingness-desc',
#                per_page=50
            )
            for photo in photos:
                secret = photo.get('secret')
                server = photo.get('server')
                id = photo.get('id')
                farm = photo.get('farm')
                size='z'
                url = r"""http://farm%s.staticflickr.com/%s/%s_%s_%s.jpg""" % (farm,server,id,secret,size)
                image = Image()
                image.url = url
                image.miracle = miracle
                image.type = 'flickr'
                image.year = year
                image.save()
    return HttpResponse()

def parse_google(request):
    miracles = Miracle.objects.all()
    years = Year.objects.all()
    for miracle in miracles:
        for year in years:
            search_title = "%s in %s "%(miracle.name,year.value)
            tag = miracle.google_tags
            search_string =urllib.quote(search_title+tag)
            #custom search zaebal
            #service = build('customsearch', 'v1', developerKey=settings.GOOGLE_API)

            #request = service.list(q=tag, cx=settings.GOOGLE_PROJECT ,searchType='image')
            #result = request.execute()

            url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % search_string)
            request = urllib2.Request(url, None, {'Referer': ''})

            response = urllib2.urlopen(request)

            results = simplejson.load(response)

            for image in results['responseData']['results']:
                try:
                    new_image = Image()
                    new_image.url= image.get('url')
                    new_image.miracle = miracle
                    new_image.type = Image.SERVICE_TYPES[2]
                    new_image.year = year
                    new_image.save(force_insert=True)
                except IntegrityError:
                    pass
            time.sleep(5)
    return HttpResponse()