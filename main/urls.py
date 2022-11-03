from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('livre/', views.livre, name= "livre"),
    path('policier/', views.livre_policier, name= "policier"),
    path('login/', views.login_page, name= "login"),
    path('logout/', views.logout_user, name= "logout"),
    path('register/', views.register_page, name="register")
]   