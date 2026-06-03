from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
    path('jobs/', include('jobs.urls')),
    path('resumes/', include('resumes.urls')),
    path('interviews/', include('interviews.urls')),
    path('goals/', include('goals.urls')),
    path('learning/', include('learning.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)