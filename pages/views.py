from django.shortcuts import render,redirect
from .models import *
import datetime
# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST['name']

        Todo = todo (
            action = name
        )
        Todo.save()
    return render(request,'pages/index.html')

def task(request):
    date_ = datetime.datetime.now()
    print(date_)
    datapending = todo.objects.filter(date_added=date_)
    datacomplete = Complete.objects.filter(date_completed=date_)

    context = {
        'datapending': datapending,
        'datacomplete':datacomplete
    }
    return render(request,'pages/tasks.html',context)

def complete(request,pk):
    if request.method=="POST":
        name = request.POST['name']

        complete_task = Complete(
            actioncomplete = name
        )
        complete_task.save()
        return redirect('/')

    task_pending = todo.objects.get(pk=pk)
    print(task_pending.action)
    task_pending.delete()
    context = {
        'task_pending' : task_pending
    }
    return render(request,'pages/complete.html',context)

def delete(request,pk):
    delete_task = todo.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        delete_task.delete()
        return redirect('/')

    context = {
        'delete_task' : delete_task
    }
    return render(request,'pages/delete.html',context)