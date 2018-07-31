from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet

user_router = routers.SimpleRouter()

user_router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    path('', include(user_router.urls)),
]
