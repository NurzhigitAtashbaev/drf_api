from django.urls import path, include
from .views import ProductViewSet, products
from rest_framework.routers import DefaultRouter
# (
#     ProductCreateAPIView,
#     ProductRetrieveAPIView,
#     ProductUpdateAPIView,
#     ProductListAPIViewpyt
# )
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    # path('create/', ProductCreateAPIView.as_view()),
    # path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
    # path('update/<int:pk>/', ProductUpdateAPIView.as_view()),
    # path('list/', ProductListAPIView.as_view()),
    path('', include(router.urls))
]
