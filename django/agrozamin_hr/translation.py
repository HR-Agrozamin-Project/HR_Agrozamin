from .models import Category, Question, ExtraCategory, ExtraQuestion
from modeltranslation.translator import TranslationOptions,register,translator

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question','A','B','C','D','ans', 'category')

@register(ExtraCategory)
class ExtraCategoryTranslationOptions(TranslationOptions):
    fields = ('extra_category_name',)

@register(ExtraQuestion)
class ExtraQuestionTranslationOptions(TranslationOptions):
    fields = ('question','A','B','C','D','ans', 'extra_category')