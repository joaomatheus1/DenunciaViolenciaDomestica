from django.shortcuts import render,redirect
from .forms import WomanForm
from .models import Woman


# Create your views here.

def paginaInicial(request):
    return render(request,"woman_register/woman_home.html")

def botao_cadastro(resquest):
    return redirect('/woman')


def woman_list(request):
    context = {'woman_list': Woman.objects.all()}
    return render(request,"woman_register/woman_list.html",context)

def woman_form(request,cpf=0):
    if request.method == "GET":
        if cpf==0:
            form = WomanForm()
        else:
            woman= Woman.objects.get(pk=cpf)
            form= WomanForm(instance=woman)
        return render(request,"woman_register/woman_form.html",{'form':form})
    else:
        if cpf==0:
            form = WomanForm(request.POST)
        else:
            woman = Woman.objects.get(pk=cpf)
            form= WomanForm(request.POST,instance= woman)
        if form.is_valid():
            form.save()
        return redirect('/woman/list')

def woman_delete(request,cpf):
    woman= Woman.objects.get(pk=cpf)
    woman.delete()
    return redirect('/woman/list')
