from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

context = Task.objects.all()

# This is a function based view which we have overridden by class based view TaskListView
def home(request):
    return render(request, 'home/home.html', {'tasks': context})


class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields = ['task']
    success_url = '/'


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['task']
    success_url = '/'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'