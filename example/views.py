
from django.views.generic import TemplateView
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from django.conf import settings

def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['from_email']
            form_message = form.cleaned_data['message']
            form_name = form.cleaned_data['name']

            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,]
            contact_message = "%s : %s via %s"%(
                form_name,
                form_message,
                form_email
            )
            try:
                send_mail(
                form_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, "index.html", {'form': form})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form_subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['from_email']
            form_message = form.cleaned_data['message']
            form_name = form.cleaned_data['name']

            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,]
            contact_message = "%s : %s via %s"%(
                form_name,
                form_message,
                form_email
            )
            try:
                send_mail(
                form_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False
                )


            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    return render(request, "contact.html", {'form': form})




class AboutPageView(TemplateView):
    template_name = "about.html"


def success(request):
    return HttpResponse('Success! Thank you for your message.')
