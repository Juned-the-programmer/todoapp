from django.shortcuts import render
from .models import *
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
    tasks = todo.objects.all()
    if request.method == "POST":
        tasks.delete()