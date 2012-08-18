from instagram.client import InstagramAPI
from django.conf import settings
from .models import Image
import flickrapi
import urllib2
import simplejson


def instagram_get_by_tag(miracle, tag):
    api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID, client_secret=settings.INSTAGTAM_SECRET)
    result = api.tag_recent_media(100, 0, tag)


    for media in result[0]:
        print media.images['standard_resolution']
        create_image(miracle, Image.SERVICE_TYPES[0], media.images['standard_resolution'], media.id)

    return

def google_get(miracle, tag):
    #custom search zaebal
    #service = build('customsearch', 'v1', developerKey=settings.GOOGLE_API)

    #request = service.list(q=tag, cx=settings.GOOGLE_PROJECT ,searchType='image')
    #result = request.execute()

    url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % (tag))

    request = urllib2.Request(url, None, {'Referer': ''})
    response = urllib2.urlopen(request)

    results = simplejson.load(response)
    for image in results['results']:
        url = image.url
        source = image.imageId
        create_image(miracle, Image.SERVICE_TYPES['google'], source)

    return

def flickr_get(object, tag):
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API)
    photos = flickr.walk(tag_mode='all',
        tags='Eifel Tower',
        min_taken_date='2011-08-20',
        max_taken_date='2012-08-26')

    import pdb
    pdb.set_trace()
    for photo in photos:

        secret = photo.get('secret')
        server = photo.get('server')
        id = photo.get('id')
        size='o'
        url = r"""http://static.flickr.com/%s/%s_%s_%s.jpg""" % (server,id,secret,size)

        create_image(miracle, Image.SERVICE_TYPES['flickr'], url, id)

        import pdb
        pdb.set_trace()
    return

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def create_image(miracle, type, url, source):

    #import pdb
    #pdb.set_trace()
    image = Image()
    image.miracle = miracle
    image.type = type
    image.url = url
    image.rating = 0
    image.source = source
    image.save()

    return image
