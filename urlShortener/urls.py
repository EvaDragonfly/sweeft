from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('shortener/', views.shortener, name = "shortener"),
    path('premium/', views.premium, name = "premium"),
    path('<str:shorted>', views.redirectUrl, name = 'redirectUrl'),
]
