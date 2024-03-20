from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_html, name="home"),
    path('<str:page_name>/', views.home_html, name="home_html")
]
