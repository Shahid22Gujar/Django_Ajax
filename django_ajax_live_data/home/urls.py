from django.urls import path
from home.views import home,get_realtime_all_users

urlpatterns = [
    path('', home,name='home'),
    path('ajax/get-all-users/', get_realtime_all_users,name='get-all-users'),
]
