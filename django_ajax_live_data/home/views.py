from django.shortcuts import render
from django.http import JsonResponse
from home.models import CustomUser

# Create your views here.
def home(request):
    return render(request, 'home.html')

def get_realtime_all_users(request):
    users=CustomUser.objects.all()[:10]
    print(list(users.values())) # by default it return queryset,so we have converted to list
    return JsonResponse({"users": list(users.values())})