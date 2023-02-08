from django.shortcuts import render

def index(request):
    return render(request, "rerouting_test/index.html")

def home(request):
    return render(request, "rerouting_test/index.html", home)

def episodes(request):
    return render(request, "rerouting_test/index.html", episodes)

def bios(request):
   return render(request, "rerouting_test/index.html", bios)

def contact(request):
    return render(request, "rerouting_test/index.html", contact)