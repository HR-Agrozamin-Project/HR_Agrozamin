from django.contrib import admin
from .models import Question, Category, ExtraQuestion, ExtraCategory
from modeltranslation.admin import TranslationAdmin


@admin.register(Question)
class QuesModelAdmin(TranslationAdmin):
    # group_fieldsets = True 
    list_display = ('question','A','B','C','D','ans', 'category')

@admin.register(Category)
class CategiryModelAdmin(TranslationAdmin):
    # group_fieldsets = True 
    list_display = ('category_name',)
    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }

@admin.register(ExtraQuestion)
class ExtraQuestionAdmin(TranslationAdmin):
    # group_fieldsets = True 
    list_display = ('question','A','B','C','D','ans', 'extra_category')

@admin.register(ExtraCategory)
class ExtraCategoryAdmin(TranslationAdmin):
    # group_fieldsets = True 
    list_display = ('extra_category_name',)



# @admin.register(Question)
# class QuestAdmin(admin.ModelAdmin):
#     model = Question
#     fields = ['title', 'document','is_activate']
#     list_display = ['title', 'document','is_activate']

#     actions = ['Habar_yuborish']

#     def Habar_yuborish(self, request, queryset):
        
#         queryset.update(is_activate=False)
#         print(queryset)


# class ImportAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/change_list.html'