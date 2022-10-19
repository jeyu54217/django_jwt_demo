
from django.contrib import admin
from django.urls import path
from .views import login, test_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/test_token', test_token),
]
