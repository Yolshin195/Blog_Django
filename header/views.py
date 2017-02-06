from django.shortcuts import render
from header.models import Header 

# Create your views here.
def headers(request):
    return render(request, 'h1.html', {"header": Header.objects.get(id=1)})
