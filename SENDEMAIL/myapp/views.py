from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError
from django.core.mail import mail_admins
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def email_success(request):
    return render(request, 'success.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            
            try:
                send_mail(
                    f'Message from {name} ({email})',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_TO_EMAIL],
                    fail_silently=False,
                )
                return HttpResponse('Email sent Successfully')
            except Exception as e:
                mail_admins(
                    'Email sending error',
                    f'Failed to send email from {email}. Error: {e}',
                )
                logger.error('Failed to send email', exc_info=e)
            
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
