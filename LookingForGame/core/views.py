from django.shortcuts import render



def home(request):
    return render(request, "core/home.html")

def lfg(request):
    return render(request, "core/lfg.html")
