from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import JobApplication
from resumes.models import Resume
from interviews.models import Interview
from goals.models import Goal
from learning.models import LearningItem

@login_required
def home(request):
    applications_count = JobApplication.objects.filter(user=request.user).count()
    resumes_count = Resume.objects.filter(user=request.user).count()
    interviews_count = Interview.objects.filter(user=request.user).count()
    goals_count = Goal.objects.filter(user=request.user).count()
    learning_count = LearningItem.objects.filter(user=request.user).count()
    context = {
        "applications_count": applications_count,
        "interviews_count": interviews_count,
        "resumes_count": resumes_count,
        "goals_count": goals_count,
        "learning_count": learning_count,
    }
    return render(request, "dashboard/home.html", context)