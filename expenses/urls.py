from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add-expenses/', views.add_expense, name='add-expenses'),
    path('update-expenses/<int:id>', views.update_expense, name='update-expense'),
    path('delete-expense', views.delete_expense, name='delete-expense'),
]