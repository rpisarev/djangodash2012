from instagram.client import InstagramAPI
from django.conf import settings
from .models import Image

def instagram_get_by_tag(object, tag):
    api = InstagramAPI(client_id=settings.INSTAGRAM_CLIENT_ID, client_secret=settings.INSTAGTAM_SECRET)
    result = api.tag_recent_media(100, 0, tag)

    for media in result[0]:
        image = Image()
        image.object = object
        image.type = image.SERVICE_TYPES['instagram']
        image.url = media.standard_resolution
        image.rating = 0
        image.source = media.id
        image.save()

    return

def google_get(object, tag):

    query = 'https://www.googleapis.com/customsearch/v1?key=%s&q=%s&searchType=image' % (settings.GOOGLE_API, tag)
    return

def flickr_get(object, tag):

    return





