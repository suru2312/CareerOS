from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Interview
from .forms import InterviewForm

@login_required
def interview_list(request):
    interviews = Interview.objects.filter(user=request.user).order_by('-interview_date')
    return render(request,'interviews/interview_list.html',{'interviews': interviews})


@login_required
def interview_create(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.user = request.user
            interview.save()
            return redirect('interview_list')
    else:
        form = InterviewForm()
    return render(request, 'interviews/interview_form.html', {'form': form})

@login_required
def interview_update(request, pk):
    interview = get_object_or_404(Interview, pk=pk, user=request.user)
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('interview_list')
    else:
        form = InterviewForm(instance=interview)
    return render(request, 'interviews/interview_form.html', {'form': form})

@login_required
def interview_delete(request, pk):
    interview = get_object_or_404(Interview, pk=pk, user=request.user)
    if request.method == "POST":
        interview.delete()
        return redirect('interview_list')
    return render(request, 'interviews/interview_confirm_delete.html', {'interview': interview})