from django.contrib import admin
from agrozamin_hr.models.usermodel import UserModel
from django.utils.translation import gettext_lazy as _
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel, SmsHistory, QuetionResult, ExtraQuetionResult
from agrozamin_hr.models.user_admin import User_admin
from agrozamin_hr.models.locations_and_number import Address, Number
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from datetime import datetime   
from django.shortcuts import render
from django import forms
import requests
import os
from django.http import HttpResponseRedirect
from .admin_mixins import ExportAsCSVMixin
from dotenv import load_dotenv
load_dotenv()

admin.site.unregister(Group)
admin.site.site_header = _("HR-Agrozamin")
admin.site.site_title = _("Agrobank ma'muriyati portali")     #"Портал администрации Агробанк")
admin.site.index_title = _("HR-Agrozamin portaliga xush kelibsiz") #"Добро пожаловать на Портал HR-Агрозамин"

admin.site.register(Address)
admin.site.register(Number)

@admin.register(User_admin)
class Admins(UserAdmin):
    fieldsets = UserAdmin.fieldsets 

class SmsHistoryAdmin(admin.TabularInline):
    model = SmsHistory
    extra = 0
    classes = ['collapse',]

class QuetionResultInline(admin.TabularInline):
    model = QuetionResult
    extra = 0
    classes = ['collapse',]

class ExtraQuetionResultInline(admin.TabularInline):
    model = ExtraQuetionResult
    extra = 0
    classes = ['collapse',]


class TextImportForm(forms.Form):
    text = forms.CharField(max_length=500, widget=forms.Textarea)

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    inlines = [SmsHistoryAdmin, QuetionResultInline, ExtraQuetionResultInline]
    group_fieldsets = True 
    list_filter = ['program_language', 'extra_skill', 'sms']
    list_display_links = ("id", 'full_name')
    list_display = ("result","id", 'full_name', "chat_id", "phone_number", "gender", "education", "age","program_language", 'cv', 'sms')
    # raw_id_fields = ['program_language', 'extra_skill']
    list_per_page = 10
    actions = ['update_status', 'export_csv']
    fieldsets = (
        (_("Shaysiy ma'lumotlar"), {
            'fields': ("chat_id","full_name", "phone_number", "gender", "education", "age","program_language", 'extra_skill', 'cv', 'sms', 'result')}),)


    def send_message(self, text, chat_id):
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=HTML"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def send_venue(self, chat_id, latitude, longitude):
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendlocation?latitude={latitude}&longitude={longitude}&chat_id={chat_id}"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def send_contact(self, chat_id, phone_number, first_name, last_name):
        url = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendContact?chat_id={chat_id}&phone_number=+998{phone_number}&first_name={first_name}&last_name={last_name}"
        payload={}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

    def update_status(self, request, queryset):
        if 'apply' in request.POST:
            print(request.POST)
            # form = TextImportForm(request.POST)
            if "True": #form.is_valid():
                text = request.POST.get('text')
                request_address = request.POST.get('address')
                request_number = request.POST.get('number')
                
                for query in  queryset.all():
                    self.send_message(chat_id=query.chat_id, text=text)

                    if request_address and request_number:
                        address = Address.objects.get(office_name=request_address)
                        self.send_venue(chat_id=query.chat_id, longitude=address.longitude, latitude=address.latitude)
                        number = Number.objects.get(number=request_number)
                        self.send_contact(chat_id=query.chat_id, phone_number=number.number, first_name=number.first_name, last_name=number.number)
                    
                    elif request_address:
                        address = Address.objects.get(office_name=request_address)
                        self.send_venue(chat_id=query.chat_id, longitude=address.longitude, latitude=address.latitude)

                    elif request_number:
                        number = Number.objects.get(number=request_number)
                        self.send_contact(chat_id=query.chat_id, phone_number=number.number, first_name=number.first_name, last_name=number.number)
                    
                    queryset.update(sms='True')
                    SmsHistory.objects.create(user=query, text=text, data=datetime.now())
                    
            self.message_user(request,
                              "Send message to {} users".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())

        address_list = Address.objects.all()
        number_list = Number.objects.all()

        data = {'orders':queryset, "address_list":address_list, "number_list":number_list}
        return render(request, 'admin/order_intermediate.html', data)

    update_status.short_description = _("Habar yuborish")


@admin.register(Question)
class QuesModelAdmin(TranslationAdmin, ExportAsCSVMixin):
    list_display = ("id",'img','question','A','B','C','D','ans', 'category')
    search_fields = ("question",)
    list_filter = ('category', )
    list_per_page = 10
    actions = ['export_csv']

@admin.register(Category)
class CategiryModelAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ("id",'category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10
    actions = ['export_csv']

@admin.register(ExtraQuestion)
class ExtraQuestionAdmin(TranslationAdmin, ExportAsCSVMixin):
    list_display = ("id",'img','question','A','B','C','D','ans', 'extra_category')
    search_fields = ('question',)
    list_filter = ['extra_category']
    list_per_page = 10
    actions = ['export_csv']

@admin.register(ExtraCategory)
class ExtraCategoryAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ("id",'extra_category_name',)
    search_fields = ('extra_category_name',)
    list_per_page = 10
    actions = ['export_csv']


