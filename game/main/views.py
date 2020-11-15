from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf.urls.static import static

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def Lv1(request):
    return render(request, 'main/Lv1.html')
                      
def Lv2(request):
    return render(request, 'main/Lv2.html')
                   
def Lv3(request):
    return render(request, 'main/Lv3.html')
    
def Lv4(request):
    return render(request, 'main/Lv4.html')  

def Lv5(request):
    return render(request, 'main/Lv5.html')  
      
def Lv6(request):
    return render(request, 'main/Lv6.html')  

def Lv7(request):
    return render(request, 'main/Lv7.html')  
        
def Lv8(request):
    return render(request, 'main/Lv8.html')  

def Result(request):
    return render(request, 'main/Result.html')  


