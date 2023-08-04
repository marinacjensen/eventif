from django.http import HttpResponseRedirect
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from django.core import mail

def subscribe(request):
    if request.method == 'POST':
        mail.send_mail('Subject',
        'Message',
        'sender@email.com',
        'visitor@email.com')
        return HttpResponseRedirect('/inscricao/')
    context = {"form": SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)