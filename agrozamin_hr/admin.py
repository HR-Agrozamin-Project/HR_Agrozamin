from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel
from agrozamin_hr.models.user_admin import User_admin
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group
admin.site.register(User_admin)
admin.site.unregister(Group)

admin.site.site_header = _("HR-Agrozamin")
admin.site.site_title = _("Agrobank ma'muriyati portali")     #"Портал администрации Агробанк")
admin.site.index_title = _("HR-Agrozamin portaliga xush kelibsiz") #"Добро пожаловать на Портал HR-Агрозамин"

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    group_fieldsets = True 
    list_display = ("first_name", "last_name", "phone_number", "gender", "education", "age","program_language", 'cv', 'test_result')
    
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