from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        return buildForm(request)
    return newForm(request)

def newForm(request, form = ContactForm()):
    return render(request, 'contact/contact_form.html', { 'form': form })

def buildForm(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return newForm(request, form)

    contextEmail = render_to_string('contact/contact_email.txt', {
        'name': form.cleaned_data['name'],
        'phone': form.cleaned_data['phone'],
        'email': form.cleaned_data['email'],
        'message': form.cleaned_data['message']
    })
    
    _send_mail('Nova mensagem!',
                contextEmail, 
                form.cleaned_data['email'],
                (settings.DEFAULT_FROM_EMAIL, form.cleaned_data['email']))

    
    messages.success(request, 'Mensagem enviada!')
    return HttpResponseRedirect('/contato/')

def _send_mail(assunto, conteudo, remetente, destinatario):
    mail.send_mail(assunto, conteudo, remetente, destinatario)

    