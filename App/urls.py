from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

# import utility module

urlpatterns = [
    # path('upload-param', views.getParamsFile, name='upload-param'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('upload-vs', views.FileUploadView.as_view(), name="upload-vs"),

]