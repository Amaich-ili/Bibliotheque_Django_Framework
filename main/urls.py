from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('livre/', views.livre, name= "livre"),
]    