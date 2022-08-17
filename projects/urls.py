from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, {'flare' : None}, name='projects'),
    path('<str:flare>/', views.projects, name='projects'),
]