from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView
# router = DefaultRouter()
# router.register('orders', )


urlpatterns = [
    # path('', include(router.urls))
    path('', UserView.as_view(), name='orders')

]