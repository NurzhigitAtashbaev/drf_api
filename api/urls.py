from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categorys', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('create/', ProductCreateAPIView.as_view()),
    # path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
    # path('update/<int:pk>/', ProductUpdateAPIView.as_view()),
    # path('list/', ProductListAPIView.as_view()),
]
