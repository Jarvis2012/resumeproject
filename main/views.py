from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def core(request):
  return render(request,'core.html',{'home':'active'})
def Save(request):
   if request.method =='POST':
        nm=request.POST.get('name')
        em=request.POST.get('email')
        msg=request.POST.get('message')
        ct=Contact(name=nm,email=em,message=msg)
        ct.save()
        messages.success(request,'THANK YOU!!!')
      #   return HttpResponse(" thank you come back again") 
   return render(request,'contact.html')

def contact(request):

   return render(request,'contact.html',{'contact':'active'})