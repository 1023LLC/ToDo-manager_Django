from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .forms import AddForm, AddUser
from .models import User, ToDo


# Create your views here
Created = ToDo.DateCreated
def index(request):
    Users = User.objects.all()
    todos = ToDo.objects.all()
    context = {'Tasks': todos, 'Users': Users}
    return render(request, 'Tasks1/index.html', context)

def Task(request, pk):
    Todo = ToDo.objects.get(id = pk)
    context = {'Tasks': Todo}
    return render(request, 'Tasks1/index.html', context)


def addTask(request):
    if (request.method == 'POST'):
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Tasks')
        else:
            form = AddForm()

    context = {'form': AddForm(), 'Created':Created}
    return render(request, 'Tasks1/addTask.html', context)



def addUser(request):
   
    if (request.method == 'POST'):
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Tasks1')
        else:
            form = AddUser()

    context = {'form': AddUser(), 'Created':Created}
    return render(request, 'Tasks1/addTask.html', context)


    


