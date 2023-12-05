from django.db.models.signals import post_save
from django.dispatch import receiver

from contact.models import Contact
from contact.views import _send_mail as sendEmail

@receiver(post_save, sender=Contact)
def reply_email(sender, instance, **kwargs):
    if instance.reply:
        subject = 'Retorno de mensagem - EventIF'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipients = [instance.email, from_email]
        template_name = 'contact/contact_response.txt'
        context = {'reply': instance}

        _send_email(subject, from_email, recipients, template_name, context)
