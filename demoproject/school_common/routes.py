from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home_Page,name='My Home Page'),
    path('about_page_id',views.About_Page,name='My About Page')
]
