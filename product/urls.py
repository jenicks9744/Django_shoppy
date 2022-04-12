from django.urls import path,include
from . import views



urlpatterns = [
    path('user',views.userdata),
    path('usrinfo',views.usrinfo)
    
]