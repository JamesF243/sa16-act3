from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def work(request):
    return render(request, 'home/work.html')

def contact(request):
    return render(request, 'home/contact.html')
