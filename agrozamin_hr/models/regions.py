from django.db import models
from django.utils.translation import gettext_lazy as _

class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name
    
    class Meta:
        verbose_name = _(u'Shahar')
        verbose_name_plural = _(u'Shaharlar')


class Region(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=30)

    @property
    def city_name(self):
        return self.city.city_name
    
    def __str__(self):
        return self.region_name
    
    class Meta:
        verbose_name = _(u'Tuman')
        verbose_name_plural = _(u'Tumanlar')