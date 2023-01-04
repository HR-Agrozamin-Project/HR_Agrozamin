from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel
from agrozamin_hr.serializers import (
    QuestionSerializer, CategorySerializer, 
    ExtraQuetionSerializer, ExtraCategorySerializer,
    UserSerializer)
import os


class UserDetailView(APIView):
    def get(self,request,*args,**kwargs):
        user_id = self.request.query_params.get("id")
        if user_id is None:
            user = UserModel.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        else:
            user = UserModel.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)        
        if serializer.is_valid():
            first_name  = f"{serializer.validated_data['first_name']}"
            last_name  = f"{serializer.validated_data['last_name']}"

            file_format_cv  = f"{serializer.validated_data['cv']}".split('.')[-1]
            file_format_test_result = f"{serializer.validated_data['test_result']}".split('.')[-1]

            serializer.validated_data['cv'].name = f"{first_name}_{last_name}_cv.{file_format_cv}"
            serializer.validated_data['test_result'].name=f'{first_name}_{last_name}_test_result.{file_format_test_result}'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionView(APIView):
    def get(self, request):
        parameter  = request.query_params.get("category_id")
        questions = Question.objects.filter(category_id=parameter)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionCheckView(APIView):
    def get(self, request):
        lan = request.query_params.get("lan")
        question_id  = request.query_params.get("question_id")
        request_answer = request.query_params.get("answer")
        question = Question.objects.get(id=question_id)
        if lan == 'ru':
            if question.ans_ru == request_answer:
                return Response(data={'response':f"True"})
            else:
                return Response(data={'response':f"False"})
        if lan == 'uz':
            if question.ans_uz == request_answer:
                return Response(data={'response':f"True"})
            else:
                return Response(data={'response':f"False"})


class ExtraCategoryView(generics.ListAPIView):
    queryset = ExtraCategory.objects.all()
    serializer_class = ExtraCategorySerializer
    
class ExrtaQuestionView(APIView):
    def get(self, request):
        parameter  = request.query_params.get("extra_category_id")
        questions = ExtraQuestion.objects.filter(extra_category_name=parameter)
        serializer = ExtraQuetionSerializer(questions, many=True)
        return Response(serializer.data)


