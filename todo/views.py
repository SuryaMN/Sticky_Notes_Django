from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . models import Todo
from . forms import TodoForm
from datetime import datetime

# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request,'todo/home.html')
    else:
        logout(request)
        message = "Succesfully logged-out"
        return render(request,'todo/home.html',{'message':message})

def loginuser(request):
    if request.method=='GET':
        return render(request,'todo/loginuser.html')
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            error = "User doesn't exist"
            return render(request,'todo/loginuser.html',{'error':error})
        else:
            login(request,user)
            return redirect(todos)

    

def signupuser(request):
    if request.method=='GET':
        return render(request,'todo/signupuser.html')
    else:
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'] , password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect(todos)
            except IntegrityError:
                error = "Username already taken. Try a new one." 
                return render(request,'todo/signupuser.html',{'error':error})
        else:
                error = "Passwords do not match" 
                return render(request,'todo/signupuser.html',{'error':error})

@login_required
def todos(request):
    if request.method=='GET':
        todos = Todo.objects.filter(user=request.user , finished_datetime__isnull = True).order_by('-created_datetime')
        return render(request,'todo/todos.html',{'todos':todos})


@login_required
def createTodo(request):
    if request.method=='GET':
        return render(request,'todo/createtodo.html',{'form':TodoForm()})
    else:
        ''' If we mention user in the ModelForm fields then it'll manually ask us to enter the user 
        .So we implement the following steps'''
        
        form = TodoForm(request.POST)               #Take input from the request.POST and store it in form
        new_todo = form.save(commit=False)          #Take input from the form and create a new todo object
        new_todo.user = request.user                #set owner of this todo to user 
        new_todo.save()                             #Save it to database
        return redirect(todos)


@login_required
def viewTodo(request,todo_id):
    todo = get_object_or_404(Todo , pk=todo_id , user=request.user)
    if request.method=='GET':
        form = TodoForm(instance=todo)
        return render(request,'todo/viewTodo.html',{'form':form , 'todo':todo})
    else:
        edited_todo = TodoForm(request.POST , instance=todo)
        edited_todo.save()
        return redirect(todos)


@login_required
def finishTodo(request,todo_id):
    todo = get_object_or_404(Todo , pk=todo_id , user=request.user)
    todo.finished_datetime = datetime.now()
    todo.save()
    return redirect(completedTodos)


@login_required
def deleteTodo(request,todo_id):
    todo = get_object_or_404(Todo , pk=todo_id , user=request.user)
    todo.delete()
    return redirect(todos)


@login_required
def completedTodos(request):
    todos = Todo.objects.filter(user=request.user , finished_datetime__isnull = False).order_by('-finished_datetime')
    return render(request,'todo/completedTodos.html',{'todos':todos})