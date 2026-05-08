from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('send/', views.send_google_auth, name='send_auth'),
    path('google/login/callback/', views.register_google_auth, name='google'),

]