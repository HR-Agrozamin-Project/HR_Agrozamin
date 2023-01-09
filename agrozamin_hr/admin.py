from django.contrib import admin
import nested_admin
from agrozamin_hr.models.usermodel import UserModel
from django.utils.translation import gettext_lazy as _
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel, QuetionResult, ExtraQuetionResult
from agrozamin_hr.models.user_admin import User_admin
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
admin.site.unregister(Group)

admin.site.site_header = _("HR-Agrozamin")
admin.site.site_title = _("Agrobank ma'muriyati portali")     #"Портал администрации Агробанк")
admin.site.index_title = _("HR-Agrozamin portaliga xush kelibsiz") #"Добро пожаловать на Портал HR-Агрозамин"


@admin.register(User_admin)
class Admins(UserAdmin):
    fieldsets = UserAdmin.fieldsets 

class QuetionResultInline(admin.TabularInline):
    model = QuetionResult
    extra = 0
    group_fieldsets = True

class ExtraQuetionResultInline(admin.TabularInline):
    model = ExtraQuetionResult
    extra = 0
    group_fieldsets = True

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    inlines = [QuetionResultInline, ExtraQuetionResultInline]
    group_fieldsets = True 
    list_display = ("id","chat_id","full_name", "phone_number", "gender", "education", "age","program_language", 'cv')
    raw_id_fields = ['program_language', 'extra_skill']
    fieldsets = (
        (_("Shaysiy ma'lumotlar"), {
            'fields': ("chat_id","full_name", "phone_number", "gender", "education", "age","program_language", 'extra_skill', 'cv')}),
        )
    list_per_page = 10

    # actions = ['Habar_yuborish']

    # def Habar_yuborish(self, request, queryset):
    #     queryset.update()
    #     print(queryset)

    
@admin.register(Question)
class QuesModelAdmin(TranslationAdmin):
    list_display = ("id",'question','A','B','C','D','ans', 'category')
    search_fields = ("question",)
    list_per_page = 10

@admin.register(Category)
class CategiryModelAdmin(admin.ModelAdmin):
    list_display = ("id",'category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ExtraQuestion)
class ExtraQuestionAdmin(TranslationAdmin):
    list_display = ("id",'question','A','B','C','D','ans', 'extra_category')
    search_fields = ('question',)
    list_per_page = 10

@admin.register(ExtraCategory)
class ExtraCategoryAdmin(admin.ModelAdmin):
    list_display = ("id",'extra_category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10


