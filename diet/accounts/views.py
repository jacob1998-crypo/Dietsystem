from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import MyModelForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'pages/homepage.html')
def register(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('login')  
    else:
        form = MyModelForm()

    return render(request, 'accounts/register.html', {'form': form})


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard') 
        else:
            messages.info(request,'username or password is incorrect')
    context={}
    return render(request,'accounts/login.html')
                
                
def logoutPage(request):
    logout(request)
    return redirect('login')