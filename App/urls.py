from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# import utility module

urlpatterns = [
    path('upload-param', views.getParamsFile, name='upload-param'),
]