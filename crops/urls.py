from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('post/', views.post_problem, name='post_problem'),
]
