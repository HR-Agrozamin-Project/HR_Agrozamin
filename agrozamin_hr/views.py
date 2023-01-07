from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from agrozamin_hr.models.categories import Category, ExtraCategory
from agrozamin_hr.models.questions import Question, ExtraQuestion
from agrozamin_hr.models.usermodel import UserModel, QuetionResult, ExtraQuetionResult
from agrozamin_hr.serializers import (
    QuestionSerializer, CategorySerializer, 
    ExtraQuetionSerializer, ExtraCategorySerializer,
    UserSerializer)
import os
import random


class UserDetailView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)       
        if serializer.is_valid():
            full_name  = f"{serializer.validated_data['full_name']}"
            first_name = full_name.split(' ')[0]
            last_name = full_name.split(' ')[1]
            file_format_cv  = f"{serializer.validated_data['cv']}".split('.')[-1]
            serializer.validated_data['cv'].name = f"{first_name}_{last_name}_cv.{file_format_cv}"
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        users = UserModel.objects.all()
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"data":"all users deleted"})

    

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionView(APIView):
    def get(self, request):
        parameter  = request.query_params.get("category_id")
        questions = Question.objects.filter(category_id=parameter).order_by('?')[:20]
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class ExtraCategoryView(generics.ListAPIView):
    queryset = ExtraCategory.objects.all()
    serializer_class = ExtraCategorySerializer
    
class ExrtaQuestionView(APIView):
    def get(self, request):
        parameters  = request.data["extra_category_id"]
        all_questions = ExtraQuestion.objects.none()
        for parameter in parameters:
            all_questions |= ExtraQuestion.objects.filter(extra_category_id=parameter).order_by('?')[:5]
        serializer = ExtraQuetionSerializer(all_questions, many=True)
        return Response(serializer.data)
        

class QuestionCheckView(APIView):

    def delete(self, request):
        chat_id = request.data['chat_id']
        user_id = UserModel.objects.get(chat_id=chat_id)

        question_results = QuetionResult.objects.filter(user=user_id)
        question_results.delete()
        extra_question_results = ExtraQuetionResult.objects.filter(user=user_id)
        extra_question_results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"data":"all users deleted"})

    def get(self, request):

        def request_question(user_id,all_json_data):
            request.data['questions']
            questions = request.data['questions']
            questions_len = len(questions)
            key_result = {}
            true_results = 0
            for key, value in questions.items():
                question = Question.objects.get(id=int(key))
                if question.ans == value:
                    result = "True"
                    key_result[key] = result
                    true_results += 1
                else:
                    result = "False"
                    key_result[key] = result
            
                QuetionResult.objects.create(
                    user=user_id, 
                    category_id=question.category, 
                    question_id=question, 
                    user_answer=value,
                    result=result
                )
            
            all_json_data["questions"]={"results":f"{key_result}", 
                                    "count_questions":questions_len, 
                                    "count_true":true_results
                              }              

        def request_extra_questions(user_id,all_json_data):
            request.data['extra_questions']
            extra_questions = request.data['extra_questions']
            extra_questions_len = len(extra_questions)
            extra_key_result = {}
            extra_true_results = 0
            for extra_key, extra_value in extra_questions.items():
                extra_question = ExtraQuestion.objects.get(id=int(extra_key))
                if extra_question.ans == extra_value:
                    result = "True"
                    extra_key_result[extra_key] = result
                    extra_true_results += 1
                else:
                    result = "False"
                    extra_key_result[extra_key] = result
            
                ExtraQuetionResult.objects.create(
                        user=user_id, 
                        extra_category_id=extra_question.extra_category, 
                        extra_question_id=extra_question, 
                        user_answer=extra_value,
                        result=result
                    )
                
            all_json_data["extra_questions"]={"results":f"{extra_key_result}", 
                                        "count_questions":extra_questions_len, 
                                        "count_true":extra_true_results
                                    }


        chat_id = request.data['chat_id']
        user_id = UserModel.objects.get(chat_id=chat_id)

        all_json_data= {}
        
        keys = list(request.data.keys())

        if ("extra_questions" in keys) and ("questions" in keys):
                request_extra_questions(user_id,all_json_data)
                request_question(user_id,all_json_data)

        elif "extra_questions" in keys:
                request_extra_questions(user_id,all_json_data)
        elif ("questions" in keys):
                request_question(user_id,all_json_data)

        return Response(data=all_json_data)


