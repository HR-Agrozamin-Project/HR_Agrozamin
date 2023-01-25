from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    office_name = models.CharField(max_length=200, null=True)
    latitude = models.FloatField() 
    longitude = models.FloatField() 

    def __str__(self):
        return self.office_name

    class Meta:
        verbose_name = _(u'Manzil')
        verbose_name_plural = _(u'Manzillar')


class Number(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    number = models.CharField(max_length=9)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = _(u'Telefon raqam')
        verbose_name_plural = _(u'Telefon raqamlar')