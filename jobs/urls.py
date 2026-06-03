from django.urls import path
from .views import job_list, job_create, job_update, job_delete

urlpatterns = [
    path('', job_list, name='job_list'),
    path('add/', job_create, name='job_create'),
    path('<int:pk>/edit/', job_update, name='job_update'),
    path('<int:pk>/delete/', job_delete, name='job_delete'),
]