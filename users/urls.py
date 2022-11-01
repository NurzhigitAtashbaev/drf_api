from django.urls import path, include
from .views import OrderView

# router = DefaultRouter()
# router.register('orders', )

urlpatterns = [
    # path('', include(router.urls))
    path('', OrderView.as_view())
]
