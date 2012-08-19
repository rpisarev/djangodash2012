import urllib2

class HeadRequest(urllib2.Request):
    def get_method(self):
        return 'HEAD'

def get_headers_only(url, redirections=True):
    opener = urllib2.OpenerDirector()
    opener.add_handler(urllib2.HTTPHandler())
    opener.add_handler(urllib2.HTTPDefaultErrorHandler())
    if redirections:
        # HTTPErrorProcessor makes HTTPRedirectHandler work
        opener.add_handler(urllib2.HTTPErrorProcessor())
        opener.add_handler(urllib2.HTTPRedirectHandler())
    try:
        res = opener.open(HeadRequest(url))
    except urllib2.HTTPError, res:
        pass
    res.close()
    return dict(headers=res.info())
