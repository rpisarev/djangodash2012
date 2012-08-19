from django.shortcuts import HttpResponse
from core.models import Year,Image,Miracle
from django.conf import settings
from django.db import IntegrityError

import flickrapi
import time
import urllib2,urllib
import simplejson


def parse(request):
    miracles = Miracle.objects.all()
    years = Year.objects.all()

    for miracles in miracles:
        parse_flickr(miracle)
        parse_google(miracle, years)
        parse_instagram(miracle)

def parse_flickr(miracle):
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API)
    photos = flickr.walk(tag_mode='all',
        tags=miracle.flickr_tags,
        min_taken_date='2010-01-01' % year,
        max_taken_date='2012-12-31' % year,
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

        create_image(miracle, Image.SERVICE_TYPES[1], url)
    return

def parse_google(miracle, years):
    for year in years:
        search_title = "%s in %s"%(miracle.google_tags, year.value)
        search_string = urllib.quote(search_title)

        #custom search feature request
        #service = build('customsearch', 'v1', developerKey=settings.GOOGLE_API)
        #request = service.list(q=tag, cx=settings.GOOGLE_PROJECT ,searchType='image')
        #result = request.execute()

        url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % search_string)
        request = urllib2.Request(url, None, {'Referer': ''})
        response = urllib2.urlopen(request)
        results = simplejson.load(response)

        for image in results['responseData']['results']:
            create_image(miracle, Image.SERVICE_TYPES[2],image.get('url'))
        time.sleep(5)
    return

def parse_instagram(miracle):
    api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID, client_secret=settings.INSTAGTAM_SECRET)

    tag = miracle.instag_tags
    result = api.tag_recent_media(100, 0, tag)

    for media in result[0]:
        create_image(miracle, Image.SERVICE_TYPES[0], media.images['standard_resolution'])
    return

def create_image(miracle, type, url, year = None):
    try:
        new_image = Image()
        new_image.miracle = miracle
        new_image.type = type
        new_image.url= url
        if year != None:
            new_image.year = year
        new_image.save()
    except IntegrityError: #not unique
        pass
    return