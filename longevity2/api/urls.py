from django.urls import include, path
from rest_framework import routers

from .views import UserViewset

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('profiles', UserViewset, basename='profiles')

urlpatterns = [
    path('', include(router_v1.urls)),
]
