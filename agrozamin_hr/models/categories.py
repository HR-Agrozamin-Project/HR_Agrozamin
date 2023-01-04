from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    class Meta:
        # verbose_name = 'Katrgoriya', _("Katrgoriya")
        verbose_name = _('Kategoriya')
        verbose_name_plural = _('Kategoriyalar')


class ExtraCategory(models.Model):
    extra_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.extra_category_name

    class Meta:
        verbose_name = _(u"Qo'shimcha kategoriya")
        verbose_name_plural = _(u"Qo'shimcha kategoriyalar")