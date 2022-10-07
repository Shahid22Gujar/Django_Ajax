
from django.urls import path
from home.views import home,get_all_users

urlpatterns = [
    path('', home,name="home"),
    path('all-users/',get_all_users,name="all-users"),
]
