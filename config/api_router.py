from django.conf import settings
from django.urls import path,include
from rest_framework.routers import DefaultRouter, SimpleRouter

from omdb_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns=[path('',include('api.urls')),]

urlpatterns += router.urls
