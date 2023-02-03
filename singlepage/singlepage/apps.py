from django.apps import AppConfig


class SinglepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'singlepage'

class ContactformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactform'