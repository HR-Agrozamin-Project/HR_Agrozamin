from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Question(models.Model):
    question = models.TextField()
    A = models.CharField(max_length=200,null=True)
    B = models.CharField(max_length=200,null=True)
    C = models.CharField(max_length=200,null=True)
    D = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class ExtraCategory(models.Model):
    extra_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.extra_category_name

    class Meta:
        verbose_name = 'Extra category'
        verbose_name_plural = 'Extra categories'

class ExtraQuestion(models.Model):
    question = models.TextField()
    A = models.CharField(max_length=200,null=True)
    B = models.CharField(max_length=200,null=True)
    C = models.CharField(max_length=200,null=True)
    D = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    extra_category = models.ForeignKey(ExtraCategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Extra question'
        verbose_name_plural = 'Extra questions'