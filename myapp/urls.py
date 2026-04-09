from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('hire/', views.hire, name='hire'),
]
