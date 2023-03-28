from django.db.models import signals
from django.dispatch import receiver
from apps.core.models import (
    Estimate
)
from django.utils import timezone 


@receiver(signals.pre_save, sender=Estimate)
def estimate_post_save(sender, instance, raw, using, *args, **kwargs):
    if instance.is_closed:
        instance.close_at = timezone.now()
