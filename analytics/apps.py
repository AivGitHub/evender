from django.apps import AppConfig
from django.core.management import call_command


class AnalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analytics'

    def ready(self):
        call_command('process', '--start')
