from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Question, Category, ExtraQuestion, ExtraCategory
from .serializers import (
    QuesSerializer, CategorySerializer, 
    ExtraQuesSerializer, ExtraCategorySerializer,
    UserSerializer, RegisterSerializer
)


#API to register user
class RegisterUserView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

#API to Get User Details using Token Authentication
class UserDetailView(APIView):
#   authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self,request,*args,**kwargs):
    print(request.user.id)
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class QuesView(APIView):
    def get(self, request):
        parameter  = request.query_params.get("category_id")
        questions = Question.objects.filter(category_id=parameter)
        serializer = QuesSerializer(questions, many=True)
        return Response(serializer.data)

class ExtraCategoryView(APIView):
    def get(self, request):
        category = ExtraCategory.objects.all()
        serializer = ExtraCategorySerializer(category, many=True)
        return Response(serializer.data)


