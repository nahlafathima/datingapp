from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from .forms import LoginFrom,UserCreationForm

# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = LoginFrom()
        return render(request, 'accounts/login.html', context)
    elif request.method == 'POST':
        form = LoginFrom(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(f'User login successfull  (username  :  {username})')
            else:
                return HttpResponse('Login failed')
        
        # If the form is not valid.
        context['form'] = form
        return render(request, 'accounts/login.html', context)

def register(request):
    context = {}
    if request.method == 'GET':
        context['form']  = UserCreationForm()
        return render(request,'accounts/register.html',context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User.objects.create_user(username=username,password=password)
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            # return HttpResponse('registation failed')
            messages.error(request, 'Registration failed. Please correct the errors below.')

        # If the form is not valid.
        context['form'] = form
        return render(request, 'accounts/registation.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request,'accounts/register.html',{'form':form})