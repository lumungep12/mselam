from django.shortcuts import render
from contact.models import feeds
from contact.models import newsMail
from contact.forms import  feedsForm
from contact.forms import newsletterForm

def contact(request):
    form = feedsForm()
    if request.method == "POST":
        form = feedsForm(request.POST)
        if form.is_valid():
            feed = feeds(
                    fullname = form.cleaned_data['fullname'],
                    mailAddr=form.cleaned_data['mailAddr'],
                    company=form.cleaned_data['company'],
                    body=form.cleaned_data['body']
                    )
            feed.save()
    context = {"form":form}
    return render(request, "contact.html", context)

def newsletter(request):
    form = newsletterForm()
    if request.method == "POST":
        form = newsletterForm(request.POST)
        if form.is_valid():
            mail = newsMail(
                    mail = form.cleaned_data['mail'],
                    )
            mail.save()
    context = {"form":form}
    return render(request, "newsletter.html", context)








