from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm          # (assumes you have one)
from django.contrib.auth.decorators import login_required  

@login_required
def home(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    return render(request, "todo/home.html", {"form": form, "todos": todos})

@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("home")


