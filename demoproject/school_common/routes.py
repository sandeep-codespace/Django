from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home_Page,name='My Home Page'),
    path('about_page_id',views.About_Page,name='My About Page'),
    path('contact_us_id',views.ContactUs_Page,name='My Contact Page'),
    path('gallery_page_id',views.Gallery_Page,name='My Gallery Page'),
    path('login_page_id',views.Login_Page,name='My Login Page')
]
