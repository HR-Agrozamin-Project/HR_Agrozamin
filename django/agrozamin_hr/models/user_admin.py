from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User_admin(AbstractUser):
    class Meta:
        verbose_name = _(u'Administrator')
        verbose_name_plural = _(u'Administratorlar')