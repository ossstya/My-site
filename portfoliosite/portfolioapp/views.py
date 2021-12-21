from django.shortcuts import render
from .models import Work, About
# Create your views here.


def home(request):
    return render(request, 'portfolioapp/home.html')


def works(request):
    my_work = Work.objects.all()
    context = {"works": my_work}
    return render(request, 'portfolioapp/works.html', context)


def work(request, pk):

    context = {}
    return render(request, 'portfolioapp/work.html')


def contact(request):


    return render(request, 'portfolioapp/contact.html')


def about(request):
    about_me = About.objects.all()
    context = {"about": about_me}
    return render(request, 'portfolioapp/about.html', context)
