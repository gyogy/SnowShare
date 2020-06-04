from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_car/', views.new_car, name='add_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('add_ride/', views.new_ride, name='add_ride'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('list/', views.listRides, name="list"),
    path('view/<int:ride_id>', views.view, name="view"),
    path('logout/', views.logoutUser, name="logout"),
    path('take_ride/', views.take_ride, name="take_ride"),
    path('resorts/', views.list_resorts, name="resorts"),
    path('resorts/<int:resort_id>', views.resort_details, name="resort_details"),
]
