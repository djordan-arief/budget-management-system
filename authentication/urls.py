from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login-page'),
    path('new-account/', views.create_new_account, name='signup'),
    path('logout/', views.logoutView, name='logout')
]