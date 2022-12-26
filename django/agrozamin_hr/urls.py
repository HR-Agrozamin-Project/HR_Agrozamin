from django.urls import path
from .views import QuesView, CategoryView, ExtraCategoryView

urlpatterns = [
    path('question/', QuesView.as_view()),
    path('category/', CategoryView.as_view()),
    path('extra-category/', ExtraCategoryView.as_view())
]