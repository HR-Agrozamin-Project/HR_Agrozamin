from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.categories import Category, ExtraCategory
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question','A','B','C','D')

@register(ExtraCategory)
class ExtraCategoryTranslationOptions(TranslationOptions):
    fields = ('extra_category_name',)

@register(ExtraQuestion)
class ExtraQuestionTranslationOptions(TranslationOptions):
    fields = ('question','A','B','C','D')
