from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.students_list, name='students_list'),
    path('students/<int:pk>/', views.students_detail, name='students_detail'),
]