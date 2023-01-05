from django.db import models
from django.core.exceptions import ValidationError
from agrozamin_hr.models.categories import Category, ExtraCategory
from django.utils.translation import gettext_lazy as _
import os

def validate_length(value,length=9):
    if value.isdigit():
        if len(str(value))!=length:
            raise ValidationError(f"Ошибка: Номер должен содержать {length} цифр.")
    else:
        raise ValidationError("Ошибка: Пишите только цифры.")

class Choice:
    class Genders(models.TextChoices):
        MALE = 'E', _('Erkak')
        FEMALE = 'A', _('Ayol')
    
    class Education(models.TextChoices):
        urta = "O'rta", _("O'rta") 
        urta_maxsus = "O'rta maxsus", _("o'rta maxsus")
        Oliy_tugallanmagan = "Oliy tugallanmagan", _("Oliy tugallanmagan")
        oliy = 'Oliy', _('Oliy')
        Magistr = "Magister", _("Magistr")
        PhD = "PhD", _("PhD")
    
    class Age(models.TextChoices):
        _18_24 = '18-24'
        _25_30 = '25-30'
        _31_35 = '31-35'
        _36_45 = '36-45'
        _46 = '46-...' 



class UserModel(models.Model):
    chat_id = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9, unique=True, validators=[validate_length])
    gender = gender = models.CharField(max_length=10, choices=Choice.Genders.choices)
    education = models.CharField(max_length=30, choices=Choice.Education.choices)
    age = models.CharField(max_length=10, choices=Choice.Age.choices)
    program_language = models.ForeignKey(Category, on_delete=models.CASCADE)
    extra_skill=models.ManyToManyField(ExtraCategory, blank=True)
    cv = models.FileField(upload_to='cv_files')

    def __str__(self):
        return self.full_name
    

    class Meta:
        verbose_name = _(u'Foydalanuvchi')
        verbose_name_plural = _(u'Foydalanuvchilar')


