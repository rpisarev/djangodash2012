from django.contrib import admin

from .models import Miracle,Image,Vote,Year

admin.site.register(Miracle)
admin.site.register(Image)
admin.site.register(Vote)
admin.site.register(Year)