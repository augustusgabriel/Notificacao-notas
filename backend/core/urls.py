from django.urls import path
from . import views

urlpatterns = [
    path('create', views.addUser),
    path('update/<str:pk>', views.updateUser),
    path('read/<str:pk>', views.getUser),
    path('delete/<str:pk>', views.deleteUser),
    path('', views.getUsers),
]