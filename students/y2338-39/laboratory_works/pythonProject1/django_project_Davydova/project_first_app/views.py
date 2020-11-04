
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def index(request):
        tasks=Task.objects.all()
        return render(request, 'project_first_app/index.html',{'title': 'Главная страница сайта', 'tasks':tasks})


def about(request):
        return render(request,'project_first_app/about.html')

def create(request):

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('general')
            form=TaskForm()
            context = {
                'form': form
            }

        return render(request,'project_first_app/create.html')

