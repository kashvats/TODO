from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import todo

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .form import regi,todotask
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        ak = regi(request.POST)
        if ak.is_valid():
            ak.save()
            return HttpResponseRedirect('/login')
    else:
        ak = regi()
        return render(request, 'registaration.html', {'pk': ak})

# login
def bogin(request):
    if request.method=='POST':
        ak = AuthenticationForm(request=request,data=request.POST)
        if ak.is_valid ():
            name = ak.cleaned_data.get('username')
            password = ak.cleaned_data.get('password')
            user = authenticate(username=name,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/add')
    else:

        gm = AuthenticationForm()
        return render(request,'login.html',{'rm':gm})

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return render(request,'logout.html')


@login_required(login_url='/login')
def Edittask(request,id):
    if request.method=='POST':
        luka = todo.objects.get(pk=id)
        pop = todotask(request.POST,instance=luka)
        if pop.is_valid():
            lop = pop.cleaned_data['Task']
            update_task = todo(id=id,Task=lop,oser=request.user)
            update_task.save()
            return HttpResponseRedirect('/add')
    else:
        luka = todo.objects.get(pk=id)
        pop = todotask(instance=luka)
        return render(request,'edittask.html',{'lopo':pop,'puka':luka})

@login_required(login_url='/login')
def add_task(request):
    if request.method == 'POST':
        al = todotask(request.POST)
        if al.is_valid():
            pok = al.cleaned_data['Task']
            save_task = todo(Task=pok,oser = request.user)
            save_task.save()
            return HttpResponseRedirect('/add')
    else:
        al = todotask()
        ret = request.user
        tosk = todo.objects.filter(oser=ret)
        return render(request,'addtask.html',{'alo':al,'flask':tosk})

@login_required(login_url='/login')
def Deletetask(request,id):
    ak = todo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/add')

def home(request):
    return render(request,'home.html')