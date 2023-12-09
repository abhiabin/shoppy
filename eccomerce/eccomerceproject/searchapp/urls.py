from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
app_name='searchapp'
urlpatterns = [


    path('',views.searchResult,name='searchResult'),



]