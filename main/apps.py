from django.apps import AppConfig
from .tasks import check_crypto_currency


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from .tasks import check_crypto_currency
        check_crypto_currency.delay()