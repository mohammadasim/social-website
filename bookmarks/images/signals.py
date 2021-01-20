from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.user_like.through)
def user_like_changed(sender, instance, **kwargs):
    """
    Function to update total_likes of the image.
    The signal is sent when m2m relationship changes.
    The m2m relationship in the image is user_like.
    In django the table representing the m2m relationship
    is called through, hence the through in the send.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.total_likes = instance.user_like.count()
    instance.save()
