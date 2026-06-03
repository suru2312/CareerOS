from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import JobApplication

@login_required
def home(request):
    applications_count = JobApplication.objects.filter(user=request.user).count()
    context = {
        "applications_count": applications_count,
        "interviews_count": 0,
        "goals_count": 0,
        "resumes_count": 0,
        "learning_count": 0,
    }
    return render(request, "dashboard/home.html", context)