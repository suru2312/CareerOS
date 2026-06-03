from django.urls import path
from .views import resume_list, resume_create, resume_delete

urlpatterns = [
    path('', resume_list, name='resume_list'),
    path('add/', resume_create, name='resume_create'),
    path('<int:pk>/delete/', resume_delete, name='resume_delete'),
]