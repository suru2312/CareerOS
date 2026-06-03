from django.urls import path
from .views import interview_list, interview_create, interview_update, interview_delete

urlpatterns = [
    path('', interview_list, name='interview_list'),
    path('add/', interview_create, name='interview_create'),
    path('<int:pk>/edit/', interview_update, name='interview_update'),
    path('<int:pk>/delete/', interview_delete, name='interview_delete'),
]