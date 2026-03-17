from django.contrib import admin
from django.urls import path
from camuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),   # important
]