from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world.")
    
def home_page(request, *args, **kwargs):
    print(request.user,"has been logged in")
    return render(request, 'home.html',{})
