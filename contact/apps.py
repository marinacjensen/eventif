from django.apps import AppConfig

class ContactConfig(AppConfig):
    name="contact"
    verbose_name="Mensagens Recebidas"

    def ready(self):
        import contact.signals