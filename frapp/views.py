from django.shortcuts import render


# Create your views here.

def frapp(request):
    return render(request, 'frapp/frapp.html')
