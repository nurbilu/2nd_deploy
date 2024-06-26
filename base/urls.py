from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('', views.index),
    path('getRoutes', views.index),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('register',views.register),
    path('products',views.ProductView.as_view()),
    path('products/<str:id>/',views.ProductView.as_view()),
    path('categories/',views.CategoryView.as_view()),
    path('categories/<str:id>/',views.CategoryView.as_view()),
    path('orders/',views.OrderView.as_view()),
]