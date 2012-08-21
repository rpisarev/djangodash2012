from django.shortcuts import HttpResponse
from django.conf import settings
from django.db import IntegrityError

import flickrapi
import time
import urllib2,urllib
import simplejson

from core.models import Year,Image,Miracle
from local.utils import get_headers_only

def parse(request):
    miracles = Miracle.objects.order_by('-id').all()
    years = Year.objects.all()

    for miracle in miracles:
        parse_flickr(miracle)
        parse_google(miracle, years)
        parse_instagram(miracle)
    return HttpResponse()

def parse_flickr(miracle):
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API)
    photos = flickr.photos_search(tag_mode='all',
        tags=miracle.flickr_tags,
        min_taken_date='2010-01-01',
        max_taken_date='2012-12-31',
        sort = 'interestingness-desc',
        per_page=settings.PARSE_FLICKR_COUNT,
    )
    for photo in photos.iter():
        secret = photo.get('secret')
        server = photo.get('server')
        id = photo.get('id')
        farm = photo.get('farm')
        size='z'
        url = r"""http://farm%s.staticflickr.com/%s/%s_%s_%s.jpg""" % (farm,server,id,secret,size)
        title = photo.get('title')

        create_image(miracle, Image.SERVICE_TYPES[1][0], url, title)
    time.sleep(2)
    return

def parse_google(miracle, years):
    for year in years:
        start = 0
        step = 4
        search_title = "%s in %s"%(miracle.google_tags, year.value)
        search_string = urllib.quote(search_title)

        #custom search feature request
        #service = build('customsearch', 'v1', developerKey=settings.GOOGLE_API)
        #request = service.list(q=tag, cx=settings.GOOGLE_PROJECT ,searchType='image')
        #result = request.execute()
        try:
            for start in xrange(start, settings.PARSE_GOOGLE_COUNT, step):
                url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&start=%i&q=%s'\
                       % (start,search_string))
                request = urllib2.Request(url, None, {'Referer': ''})
                response = urllib2.urlopen(request)
                results = simplejson.load(response)

                if results:
                    if results['responseData']['results'] is not None:
                        for image in results['responseData']['results']:
                            title = image.get('titleNoFormatting')
                            if len(image.get('url'))<250:
                                create_image(miracle, Image.SERVICE_TYPES[2][0],image.get('url'), title,year)
                time.sleep(3)
        except:
            pass
    return

def parse_instagram(miracle):
    tag = miracle.instagram_tags
    count = 20
    next_url = 'https://api.instagram.com/v1/tags/%s/media/recent?count=%s&max_id=0&client_id=%s' % (tag, count, settings.INSTAGRAM_CLIENT_ID)
    for i in xrange(1, settings.PARSE_INSTAGRAM_COUNT):
        try:
            if next_url:
                request = urllib2.Request(next_url, None, {'Referer': ''})
                response = urllib2.urlopen(request)
                results = simplejson.load(response)

                if not results:
                    break
                
                next_url = results['pagination'].get('next_url',False)

                for media in results['data']:
                    url = media['images']['standard_resolution']['url']
                    title = miracle.name
                    if media['caption']:
                        title = media['caption']['text']

                    create_image(miracle, Image.SERVICE_TYPES[0][0], url, title)

                time.sleep(2)
            else:
                break
        except:
            pass #time is end
    return

def create_image(miracle, type, url, title, year = None):
    try:
        new_image = Image()
        new_image.miracle = miracle
        new_image.type = type
        new_image.url = url
        new_image.title = title
        if year is not None:
            new_image.year = year
        new_image.save()
    except : #not unique or contains invalid characters
        pass
    return

def clean_images(request):
    images = Image.objects.all()
    deleted = 0
    for image in images:
        try:
            headers = get_headers_only(image.url)
        except urllib2.URLError:
            image.delete()
            deleted+=1
            continue
        if not headers.get('content-type','').find('image')>-1:
            image.delete()
            deleted+=1
    return HttpResponse("%i images deleted " % deleted)
