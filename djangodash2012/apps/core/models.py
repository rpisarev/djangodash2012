from django.db import models

# Create your models here.
class Miracle(models.Model):
    name = models.CharField('Name',max_length=250)
    description = models.TextField('Description')
    coord_x = models.CharField('Latitude',max_length=250)
    coord_y = models.CharField('Longitude',max_length=250)
    instag_tags = models.CharField('Instagram tags',max_length=250)
    google_tags = models.CharField('Google tags',max_length=250)
    flickr_tags = models.CharField('Flickr tags',max_length=250)
    slug = models.SlugField('Slug',max_length=250)

    def __unicode__(self):
        return self.name

class Year(models.Model):
    value = models.IntegerField()

    def __unicode__(self):
        return unicode(self.value)

class Image(models.Model):
    SERVICE_TYPES = (
        ('instagram', 'Instagram'),
        ('flickr', 'Flickr'),
        ('google', 'Google'),
        )
    rating = models.IntegerField('Rating',default=0)
    type = models.CharField('Service type',max_length=20,choices=SERVICE_TYPES)
    url = models.URLField('URL',max_length=250,unique=True)
    source = models.CharField('Source Id', max_length=250,unique=True)

    miracle = models.ForeignKey(Miracle)
    year =models.ForeignKey(Year)

    def __unicode__(self):
        return  self.url

class Vote(models.Model):
    value = models.DecimalField(default = 1,decimal_places=0,max_digits=1)
    user_ip = models.CharField("User IP",max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    image = models.ForeignKey(Image)

    def __unicode__(self):
        return str(self.value)