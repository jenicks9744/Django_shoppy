"""mysiteone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from django.http import HttpResponse

import home
from home import urls
    

# or import home 

# def home(request):
#     return HttpResponse("<h1>Hi my name is Jenicks</h1>")
############################################

# def homeone(request):
#     return render(request,'home.html')
#############################################
# this homeone function is cut and paste it into views
import product
from product import urls


from django.template import loader



def land(request):
        datasample= loader.get_template('landingpage.html')
        data={}
        response=datasample.render(data,request)
        return HttpResponse(response)




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home),
    path('',land),
    path('home/',include(home.urls)),
    path('product/',include(product.urls))
]
