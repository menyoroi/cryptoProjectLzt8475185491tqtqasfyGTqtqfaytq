from django.core.signals import request_started
from django.dispatch import receiver
from .tasks import check_crypto_currency


@receiver(request_started)
def on_request_started(sender, **kwargs):
    check_crypto_currency.delay()