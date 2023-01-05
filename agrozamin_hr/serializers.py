from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models.categories import Category, ExtraCategory
from .models.questions import Question, ExtraQuestion
from .models.usermodel import UserModel

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserModel
    fields = ("id","chat_id","full_name", "phone_number", "gender", "education", "age","program_language", "extra_skill", "cv")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','question','A','B','C','D','category')

class ExtraCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCategory
        fields = ('id','extra_category_name')

class ExtraQuetionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraQuestion
        fields = ('id','question','A','B','C','D','extra_category')


