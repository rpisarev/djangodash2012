import datetime

def set_cookie(response, key, value, days_expire):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() \
    + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key=str(key), value=value,expires=expires, max_age=max_age)