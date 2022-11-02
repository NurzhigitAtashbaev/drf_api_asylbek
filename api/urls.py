from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (
    # ProductCreateAPIView,
    # ProductDetailView,
    # UpdateProductView,
    # ProductListAPIView
    ProductViewSet
)

router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    # path('product-update/<int:pk>/', UpdateProductView.as_view()),
    # path('product-list/', ProductListAPIView.as_view()),
]
