
from django.contrib import admin
from django.urls import path
from .views import login, test_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/test_api', test_api),
]
