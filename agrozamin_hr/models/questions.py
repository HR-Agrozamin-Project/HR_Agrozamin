from django.db import models
from agrozamin_hr.models.categories import Category, ExtraCategory
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    img = models.ImageField(null=False, blank=True)
    question = models.TextField()
    A = models.CharField(max_length=200,null=True)
    B = models.CharField(max_length=200,null=True)
    C = models.CharField(max_length=200,null=True)
    D = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _(u'Savol')
        verbose_name_plural = _(u'Savollar')


class ExtraQuestion(models.Model):
    img = models.ImageField(null=False, blank=True)
    question = models.TextField()
    A = models.CharField(max_length=200,null=True)
    B = models.CharField(max_length=200,null=True)
    C = models.CharField(max_length=200,null=True)
    D = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    extra_category = models.ForeignKey(ExtraCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
        
    class Meta:
        verbose_name = _(u"Qo'shimcha savol")
        verbose_name_plural = _("Qo'shimcha savollar")