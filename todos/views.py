from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoCreate
from django.http import HttpResponse
#DataFlair
def index(request):
    todos = Todo.objects.all()
    return render(request, 'library.html', {'todos': todos})
def create(request):
    upload = TodoCreate()
    if request.method == 'POST':
        upload = TodoCreate(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})
def update(request,id):
    id = int(id)
    try:
        todo = Todo.objects.get(id =id)
    except Todo.DoesNotExist:
        return redirect('index')
    form = TodoCreate(request.POST or None, instance = todo)
    if form.is_valid():
       form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':form})
def delete(request,id):
    id = int(id)
    try:
        todo = Todo.objects.get(id = id)
    except Todo.DoesNotExist:
        return redirect('index')
    todo.delete()
    return redirect('index')