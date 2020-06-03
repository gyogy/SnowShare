from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_car/', views.new_car, name='add_car'),
    path('add_ride/', views.new_ride, name='add_ride'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
