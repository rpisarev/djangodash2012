from django.contrib import admin

from .models import Object,Image,Vote,Year

admin.site.register(Object)
admin.site.register(Image)
admin.site.register(Vote)
admin.site.register(Year)