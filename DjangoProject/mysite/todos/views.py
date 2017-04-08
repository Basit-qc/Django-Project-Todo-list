# Standard Imports
import json

# Third Party
from django.shortcuts import render
from django.http import HttpResponse

# Application Specific
from models import TodoTask
from todos.forms import AddTodoForm


def index(request):
    return HttpResponse("Hello, world. You're at the todos index.")


def add_todo_form(request):
    """ add todo task to database """
    if request.method == 'POST':
        added_summary = request.POST['task_name']
        added_description = request.POST['description']
        add = TodoTask(task_name=added_summary,
                       description=added_description)
        add.save()
        return HttpResponse(json.dumps({'response': 'Form saved'}))
    else:
        return HttpResponse('%s method not allowed' % request.method)


def todo_list(request):
    """
    This view returns all the TODOs present in database table TodoTask
    """
    all_todos = TodoTask.objects.all()
    form = AddTodoForm()
    return render(request, 'todos/all_todos.html',
                  {'all_todos': all_todos,
                   'form': form
                   })


def resolve(request):
    """
    This view will mark the requested task as resolved
    """
    if request.method == 'POST':
        task = TodoTask.objects.get(pk=request.POST['task_id'])
        # toggle value of is_checked
        task.is_checked = not task.is_checked
        task.save()
        return HttpResponse(json.dumps({'response': 'Task updated'}))
