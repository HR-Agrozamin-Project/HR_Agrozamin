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
        request_answer = request.query_params.get("answer")
        if request.query_params.get("question_id"):
            question_id  = request.query_params.get("question_id")
            try:
                question = Question.objects.get(id=question_id)
                if question.ans == request_answer:
                    return Response(data={
                        'response':f"True", 
                        "category":f"{question.category}", 
                        "question_id":f"{question_id}", 
                        'answer':f'{request_answer}'
                        })
                else:
                    return Response(data={
                        'response':f"False", 
                        "category":f"{question.category}", 
                        "question_id":f"{question_id}", 
                        'answer':f'{request_answer}'
                        })
            except Question.DoesNotExist:
                content = {'question': 'question does not exist'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            
        elif request.query_params.get("extra_question_id"):
            extra_question_id = request.query_params.get("extra_question_id")
            try:
                question = ExtraQuestion.objects.get(id=extra_question_id)
                if question.ans == request_answer:
                    return Response(data={
                        'response':f"True", 
                        "extra_category":f"{question.extra_category}", 
                        "extra_question_id":f"{extra_question_id}", 
                        "answer":f"{request_answer}"
                        })
                else:
                    return Response(data={
                        'response':f"False", 
                        "extra_category":f"{question.extra_category}", 
                        "extra_question_id":f"{extra_question_id}", 
                        'answer':f'{request_answer}'
                        })
            except ExtraQuestion.DoesNotExist:
                content = {'extra_question': 'extra_question does not exist'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
        

class ExtraCategoryView(generics.ListAPIView):
    queryset = ExtraCategory.objects.all()
    serializer_class = ExtraCategorySerializer
    
class ExrtaQuestionView(APIView):
    def get(self, request):
        parameter  = request.query_params.get("extra_category_id")
        questions = ExtraQuestion.objects.filter(extra_category_name=parameter)
        serializer = ExtraQuetionSerializer(questions, many=True)
        return Response(serializer.data)


