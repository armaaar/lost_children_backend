from django.apps import AppConfig


class HealthConfig(AppConfig):
    """Class for app registeration with django"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health'
