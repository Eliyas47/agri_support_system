from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('post/', views.post_problem, name='post_problem'),
    path('problems/', views.problem_list, name='problem_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
