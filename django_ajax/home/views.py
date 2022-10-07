from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        User.objects.create_user(username=username, password=password)
        return HttpResponse("Profile created successfully" + " " + username)
    return render(request, 'home.html')

def get_all_users(request):
    context={'users':User.objects.all()}
    return render(request, 'all_users.html', context=context)


