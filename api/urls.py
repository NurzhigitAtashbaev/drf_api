from django.urls import path, include
from .views import ProductCreateView

urlpatterns = [
    path('create/', ProductCreateView.as_view()),
]