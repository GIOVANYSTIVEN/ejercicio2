from django.shortcuts import render, redirect

# Create your views here.
from .models import Tarea
from .form import TareaForm

def crear (request):
    if request.method =='POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
        form = TareaForm()
        return render(request,'crear.html',{'form':form})
    
    def listar (request):
        tareas = Tarea.objects.all()
        return render(request,'listar.html',{'tareas':tareas})