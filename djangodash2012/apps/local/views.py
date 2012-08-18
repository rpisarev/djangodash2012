from django.shortcuts import HttpResponse
from core.models import Year,Image,Miracle
from django.conf import settings

import flickrapi

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