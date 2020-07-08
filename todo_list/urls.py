"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.loginuser,name="loginuser"),
    path('signup/',views.signupuser,name="signupuser"),
    path('todos/',views.todos,name="todos"),
    path('todos/createTodo/',views.createTodo,name="createTodo"),
    path('todos/viewTodo/<int:todo_id>/',views.viewTodo,name="viewTodo"),
    path('todos/finishTodo/<int:todo_id>',views.finishTodo,name="finishTodo"),
    path('todos/deleteTodo/<int:todo_id>',views.deleteTodo,name="deleteTodo"),
    path('todos/completedTodos/',views.completedTodos,name="completedTodos"),
]
