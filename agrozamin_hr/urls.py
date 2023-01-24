from django.urls import path
from .views import (
    CategoryView, QuestionView, 
    ExtraCategoryView, ExrtaQuestionView,
    UserView, UserDetailView, QuestionCheckView
)

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('question/', QuestionView.as_view()),
    path('extra-category/', ExtraCategoryView.as_view()),
    path('extra-question/', ExrtaQuestionView.as_view()),
    path('register/', UserView.as_view()),
    path('user/', UserDetailView.as_view()),
    path('check/', QuestionCheckView.as_view()),
]