from django.shortcuts import render
from .models import Work, About, Contact
from .services.notion import save_contact_at_notion_database
# Create your views here.


def home(request):
    return render(request, 'portfolioapp/home.html')


def works(request):
    my_work = Work.objects.all()
    context = {"works": my_work}
    return render(request, 'portfolioapp/works.html', context)


def work(request, pk):
    the_work = Work.objects.get(pk=pk)
    context = {"work": the_work}
    return render(request, 'portfolioapp/work.html', context)


def contact(request):
    if request.method == "POST":
        Contact.objects.create(email=request.POST.get("email_input"),
                               message=request.POST.get("message_input"),
                               subject=request.POST.get("subject_input"))

        save_contact_at_notion_database(email=request.POST.get("email_input"),
                                        message=request.POST.get("message_input"),
                                        subject=request.POST.get("subject_input"))

    return render(request, 'portfolioapp/contact.html')


def about(request):
    about_me = About.objects.all()
    context = {"about": about_me}
    return render(request, 'portfolioapp/about.html', context)
