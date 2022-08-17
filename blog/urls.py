from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, {'post_flare' : None}, name='blog'),
    path('<str:post_flare>/', views.blog, name='blog'),
]