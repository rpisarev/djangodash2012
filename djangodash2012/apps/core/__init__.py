from django.db.models.signals import post_syncdb
from core.models import Year, Miracle
import core.models
from django.conf import settings

def initial_years(sender, **kwargs):
    if Year in kwargs.get('created_models'):
        for year in xrange(settings.INITIAL_YEAR,settings.FINAL_YEAR,settings.YEAR_STEP):
            new_year = Year()
            new_year.value = year
            new_year.save()

def initial_miracles(sender, **kwargs):

    """
    Predefined miracles
    """
    miracles = (
        {"name":"Eifell Tower", "instagram_tags":"eifelltower", "google_tags":"eifell tower",
         "flickr_tags":"eifell tower", "slug":"eifell_tower", "description":"",},

        {"name":"Colosseum", "instagram_tags":"colosseum", "google_tags":"colosseum",
         "flickr_tags":"colosseum", "slug":"colosseum", "description":"",},

        {"name":"Taj Mahal", "instagram_tags":"tajmahal", "google_tags":"taj mahal",
         "flickr_tags":"taj mahal", "slug":"taj_mahal", "description":"",},

        {"name":"Cristo Redentor", "instagram_tags":"cristoredentor", "google_tags":"cristo redentor",
         "flickr_tags":"cristo redentor", "slug":"cristo_redentor", "description":"",},

        {"name":"Giza Pyramid", "instagram_tags":"giza", "google_tags":"giza pyramid",
         "flickr_tags":"giza pyramid", "slug":"giza_pyramid", "description":"",},

        {"name":"Statue of Liberty", "instagram_tags":"statueofliberty", "google_tags":"statue of liberty",
         "flickr_tags":"statue of liberty", "slug":"statue_of_liberty", "description":"",},

        {"name":"Big Ben", "instagram_tags":"bigben", "google_tags":"big ben",
         "flickr_tags":"big ben", "slug":"big_ben", "description":"",},

        {"name":"Neuschwanstein Castle", "instagram_tags":"neuschwanstein", "google_tags":"neuschwanstein castle",
         "flickr_tags":"neuschwanstein castle", "slug":"neuschwanstein_castle", "description":"",},

        {"name":"Red Square", "instagram_tags":"redsquare", "google_tags":"red square",
         "flickr_tags":"red square", "slug":"red_square", "description":"",},

        {"name":"Acropolis of Athens", "instagram_tags":"acropolis", "google_tags":"acropolis of athens",
         "flickr_tags":"acropolis", "slug":"acropolis_of_athens", "description":"",},

        {"name":"Alhambra", "instagram_tags":"alhambra", "google_tags":"alhambra",
         "flickr_tags":"alhambra", "slug":"alhambra", "description":"",},

        {"name":"Moai Statues", "instagram_tags":"moai", "google_tags":"moai statues",
         "flickr_tags":"moai statues", "slug":"moai_statues", "description":"",},

        {"name":"Stonehenge", "instagram_tags":"stonehenge", "google_tags":"stonehenge",
         "flickr_tags":"stonehenge", "slug":"stonehenge", "description":"",},

        {"name":"Ayasofya", "instagram_tags":"ayasofya", "google_tags":"ayasofya",
         "flickr_tags":"ayasofya", "slug":"ayasofya", "description":"",},
    )

    if Miracle in kwargs.get('created_models'):
        for miracle in miracles:
            new_miracle = Miracle()
            new_miracle.name = miracle['name']
            new_miracle.description = miracle['description']
            new_miracle.instagram_tags = miracle['instagram_tags']
            new_miracle.google_tags = miracle['google_tags']
            new_miracle.flickr_tags = miracle['flickr_tags']
            new_miracle.slug = miracle['slug']
            new_miracle.save()


post_syncdb.connect(initial_years, sender=core.models)
post_syncdb.connect(initial_miracles, sender=core.models)