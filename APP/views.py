from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'APP/home.html')

def about(request):
    return render(request, 'APP/about.html')

def contact(request):
    return render(request, 'APP/contact.html')
