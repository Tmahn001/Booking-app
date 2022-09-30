from django.apps import AppConfig
from django.conf import settings


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    def ready(self):
        #print("starting scheduler")
        from . import run
        from .run import startjob
        

        	
