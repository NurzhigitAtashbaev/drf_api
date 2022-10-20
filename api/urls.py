from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('create/', ProductView.as_view()),
]