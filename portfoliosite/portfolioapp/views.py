from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'portfolioapp/home.html')


def works(request):
    return render(request, 'portfolioapp/works.html')


def work(request, pk):
    return render(request, 'portfolioapp/work.html')


def contact(request):
    return render(request, 'portfolioapp/contact.html')


def about(request):
    return render(request, 'portfolioapp/about.html')