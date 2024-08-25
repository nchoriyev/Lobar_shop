from django.urls import path, include
from rest_framework import routers

from .views import home, shop, contact, detail, order_create_view, detail_featured

# router = routers.DefaultRouter()
# router.register(r'orders', OrderListCreateAPIView, basename='orders')

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('<int:id>/detail', detail, name='detail'),
    path('<int:id>/order', order_create_view, name='order'),
    path('detail_featured_products/', detail_featured, name='detail_featured_products'),
    # path('', include(router.urls)),
]
