from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LearningItem
from .forms import LearningItemForm

@login_required
def learning_list(request):
    items = LearningItem.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'learning/learning_list.html', {'items': items})

@login_required
def learning_create(request):
    if request.method == 'POST':
        form = LearningItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('learning_list')
    else:
        form = LearningItemForm()
    return render(request, 'learning/learning_form.html', {'form': form})

@login_required
def learning_update(request, pk):
    item = get_object_or_404(LearningItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LearningItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('learning_list')
    else:
        form = LearningItemForm(instance=item)
    return render(request, 'learning/learning_form.html', {'form': form})

@login_required
def learning_delete(request, pk):
    item = get_object_or_404(LearningItem, pk=pk, user=request.user)
    if request.method == "POST":
        item.delete()
        return redirect('learning_list')
    return render(request, 'learning/learning_confirm_delete.html', {'item': item})