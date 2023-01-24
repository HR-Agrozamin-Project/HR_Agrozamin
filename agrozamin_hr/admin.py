from django.contrib import admin
import nested_admin
from agrozamin_hr.models.usermodel import UserModel
from django.utils.translation import gettext_lazy as _
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel, SmsHistory, QuetionResult, ExtraQuetionResult
from agrozamin_hr.models.user_admin import User_admin
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from datetime import datetime   
from django.shortcuts import render
from django import forms
import requests
import os
from django.http import HttpResponseRedirect

from dotenv import load_dotenv
load_dotenv()

admin.site.unregister(Group)
admin.site.site_header = _("HR-Agrozamin")
admin.site.site_title = _("Agrobank ma'muriyati portali")     #"Портал администрации Агробанк")
admin.site.index_title = _("HR-Agrozamin portaliga xush kelibsiz") #"Добро пожаловать на Портал HR-Агрозамин"



@admin.register(User_admin)
class Admins(UserAdmin):
    fieldsets = UserAdmin.fieldsets 

class SmsHistoryAdmin(admin.TabularInline):
    model = SmsHistory
    extra = 0
    group_fieldsets = True

class QuetionResultInline(admin.TabularInline):
    model = QuetionResult
    extra = 0
    group_fieldsets = True

class ExtraQuetionResultInline(admin.TabularInline):
    model = ExtraQuetionResult
    extra = 0
    group_fieldsets = True

class TextImportForm(forms.Form):
    text = forms.CharField(max_length=500, widget=forms.Textarea)

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    inlines = [SmsHistoryAdmin, QuetionResultInline, ExtraQuetionResultInline]
    group_fieldsets = True 
    list_filter = ['program_language', 'extra_skill', 'sms']
    list_display_links = ("id", 'full_name')
    list_display = ("id", 'full_name', "chat_id", "phone_number", "gender", "education", "age","program_language", 'cv', 'sms', 'result')
    raw_id_fields = ['program_language', 'extra_skill']
    list_per_page = 10
    actions = ['update_status']
    fieldsets = (
        (_("Shaysiy ma'lumotlar"), {
            'fields': ("chat_id","full_name", "phone_number", "gender", "education", "age","program_language", 'extra_skill', 'cv', 'sms', 'result')}),)
    
    def user(self, obj):
        return obj.full_name,
    user.allow_tags = True


    def send_message(self, text, chat_id):
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=HTML"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def send_venue(self, chat_id):
        latitude = 41.29490869112361
        longitude = 69.2182447025784
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendlocation?latitude={latitude}&longitude={longitude}&chat_id={chat_id}"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def send_contact(self, chat_id):
        phone_number='+998781500088'
        first_name='Durdona'
        last_name='HR'
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendContact?chat_id={chat_id}&phone_number={phone_number}&first_name={first_name}&last_name={last_name}"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def update_status(self, request, queryset):
        if 'apply' in request.POST:
            form = TextImportForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data.get('text')
                for query in  queryset.all():
                    self.send_message(chat_id=query.chat_id, text=text)
                    self.send_venue(chat_id=query.chat_id)
                    self.send_contact(chat_id=query.chat_id)
                    queryset.update(sms='True')
                    SmsHistory.objects.create(user=query, text=text, data=datetime.now())
                    
            self.message_user(request,
                              "Send message to {} users".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())

        form = TextImportForm()
        data = {'form':form, 'orders':queryset}
        return render(request,
                      'admin/order_intermediate.html',
                      data)

    update_status.short_description = _("Habar yuborish")


@admin.register(Question)
class QuesModelAdmin(TranslationAdmin):
    list_display = ("id",'img','question','A','B','C','D','ans', 'category')
    search_fields = ("question",)
    list_filter = ('category', )
    list_per_page = 10

@admin.register(Category)
class CategiryModelAdmin(admin.ModelAdmin):
    list_display = ("id",'category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10

@admin.register(ExtraQuestion)
class ExtraQuestionAdmin(TranslationAdmin):
    list_display = ("id",'img','question','A','B','C','D','ans', 'extra_category')
    search_fields = ('question',)
    list_filter = ['extra_category']
    list_per_page = 10

@admin.register(ExtraCategory)
class ExtraCategoryAdmin(admin.ModelAdmin):
    list_display = ("id",'extra_category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10


