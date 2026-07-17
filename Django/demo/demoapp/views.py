from django.shortcuts import render 
from django.http import HttpResponse
from django.views import View

from .forms import reservationForm  
# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")


class helloindia(View ):
    def get(self,request):
        return HttpResponse("hello india")
    
    
   
    def home(request):
        form = reservationForm()
        if request.method == 'POST':
            form = reservationForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponse("Sucess")
        return render(request,'index.html',{'form' : form})