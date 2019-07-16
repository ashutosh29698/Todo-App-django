from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {
        'todo_list' : todo_list,
        'form':form
    }
    return render(request,'TodoApp/index.html',context)

@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if(form.is_valid()):
        new_todo = Todo( text = form.cleaned_data['text'] )
        new_todo.save()
    return redirect('index')

def complete_todo(request,todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.isComplete = True
    todo.save()
    return redirect('index')

def delete_completed(request):
    todo = Todo.objects.filter(isComplete = True)
    todo.delete()
    return redirect('index')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')