from django.urls import path
from .views import learning_list, learning_create, learning_update, learning_delete

urlpatterns = [
    path('', learning_list, name='learning_list'),
    path('add/', learning_create, name='learning_create'),
    path('<int:pk>/edit/', learning_update, name='learning_update'),
    path('<int:pk>/delete/', learning_delete, name='learning_delete'),
]