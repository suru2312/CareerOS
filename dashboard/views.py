from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        "applications_count": 0,
        "interviews_count": 0,
        "goals_count": 0,
        "resumes_count": 0,
        "learning_count": 0,
    }
    return render(request, "dashboard/home.html", context)