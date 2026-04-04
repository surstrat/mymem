from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .forms import ReminderForm

@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(created_by=request.user).order_by('-send_at')
    return render(request, 'reminders/list.html', {'reminders': reminders})

@login_required
def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.created_by = request.user

            if reminder.recipient_type == 'self':
                reminder.recipient_user = request.user

            reminder.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/create.html', {'form': form})

@login_required
def reminder_edit(request, pk):
    reminder = Reminder.objects.get(pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            reminder = form.save(commit=False)
            if reminder.recipient_type == 'self':
                reminder.recipient_user = request.user
            reminder.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/edit.html', {'form': form, 'reminder': reminder})

@login_required
def reminder_delete(request, pk):
    reminder = Reminder.objects.get(pk=pk, created_by=request.user)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminders/delete.html', {'reminder': reminder})