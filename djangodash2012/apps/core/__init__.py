from django.db.models.signals import post_syncdb
from core.models import Year
import core.models
from django.conf import settings

def initial_years(sender, **kwargs):
    if Year in kwargs.get('created_models'):
        for year in xrange(settings.INITIAL_YEAR,settings.FINAL_YEAR,settings.YEAR_STEP):
            new_year = Year()
            new_year.value = year
            new_year.save()

post_syncdb.connect(initial_years, sender=core.models)