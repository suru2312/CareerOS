from django.urls import path
from .views import goal_list, goal_create, goal_update, goal_delete

urlpatterns = [
    path('', goal_list, name='goal_list'),
    path('add/', goal_create, name='goal_create'),
    path('<int:pk>/edit/', goal_update, name='goal_update'),
    path('<int:pk>/delete/',goal_delete, name='goal_delete'),
]