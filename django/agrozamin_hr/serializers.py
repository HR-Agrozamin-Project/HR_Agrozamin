from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import Question, Category, ExtraCategory,ExtraQuestion

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name"]

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  confirm_password = serializers.CharField(write_only=True, required=True)

  class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'confirm_password')
        extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True}}

  def validate(self, attrs):
    if attrs['password'] != attrs['confirm_password']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = User.objects.create(
        username=validated_data['first_name'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category_name')

class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question','A','B','C','D','ans', 'category')

class ExtraCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCategory
        fields = ('id','extra_category_name')

class ExtraQuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraQuestion
        fields = ('question','A','B','C','D','ans', 'extra_category')

