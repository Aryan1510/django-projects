
from django.urls import path
from home import views


urlpatterns = [
    path('home', views.home, name='home'),  # Home page
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

]
