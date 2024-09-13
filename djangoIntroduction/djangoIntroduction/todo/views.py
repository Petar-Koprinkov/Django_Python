from django.http import Http404
from django.shortcuts import render
from djangoIntroduction.todo.models import Tasks


def index(request):
    task_filter = request.GET.get('filter', '')
    tasks = Tasks.objects.filter(name__contains=task_filter)

    context = {
        'tasks': tasks,
        'task_filter': task_filter
    }

    return render(request, 'todo/index.html', context)


def error(request):
    raise Http404


