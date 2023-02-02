from django.apps import AppConfig

class SinglepageConfig(AppConfig):
    name = 'singlepage'
    
class ContactformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactform'