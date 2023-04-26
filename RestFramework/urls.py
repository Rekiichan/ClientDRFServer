from App.views import home
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    # path('admin/', admin.site.urls),
    path('api/', include("App.urls")),
]

