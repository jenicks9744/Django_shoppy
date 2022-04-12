from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def userdata(request):
        datasample= loader.get_template('userdetails.html')
        data={}
        response=datasample.render(data,request)
        return HttpResponse(response)

from .models import userinfo

def usrinfo(request):
        # print(request.POST['name'])
        user = userinfo(
                name=request.POST["na"],
                email=request.POST["eml"],
                password=request.POST["pass"],
                phone=request.POST["ph"])
        user.save()

        return HttpResponse('user created')