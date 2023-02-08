from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

#create views here

def index(request):
    return render(request, "singlepage/index.html")

def home(request):
    return render(request, "singlepage/index.html", home)

def episodes(request):
    return render(request, "singlepage/index.html", episodes)

def bios(request):
   return render(request, "singlepage/index.html", bios)

def contact(request):
    return render(request, "singlepage/index.html", contact)

def form(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return redirect ("/contact?submitted=True")
	else:
		form = ContactForm()
		if submitted in request.GET:
			submitted = True
   
	return render(request, "index.html", {'form':form, "submitted": submitted})