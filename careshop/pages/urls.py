from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('<slug:slug>',views.detaylar , name="urun_detaylar"),



]