from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, RequestContext,HttpResponseRedirect

def main(request,template='main.html'):
    context = ({})
    return render(request, template, context)

def object(request,obj_slug):
    return  HttpResponse()

def object_year(request,obj_slug,year):
    return HttpResponse()

def test_google(request):
    return HttpResponse()

def test_instagram(request):
    return HttpResponse()

def test_flickr(request):
    import flickrapi
    api_key = '333ecc67971ffa129d1e24f56eb45a3a'
    flickr = flickrapi.FlickrAPI(api_key)
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
        import pdb
        pdb.set_trace()
    return HttpResponse()