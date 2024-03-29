from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Marina Jensen",  
                    email="marina.jensen@mail.com",
                    phone='53 91234-5678',
                    message='Olá mundo!')
        
        self.response = self.client.post('/contato/', data)

    def test_contact_post(self):
        self.assertEqual(302, self.response.status_code)

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))

class ContactPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/contato/', {})

    def test_contact_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_contact_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    def test_contact_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_contact_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class ContactEmailValid(TestCase):
    def setUp(self):
        data = dict(name="Marina Jensen",  
                    email="marina.jensen@mail.com",
                    phone='53 91234-5678',
                    message='Olá mundo!')
        
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]


    def test_contact_email_subject(self):
        esperado = "Nova mensagem!"
        self.assertEqual(esperado, self.email.subject)

    def test_contact_email_sender(self):
        esperado = "marina.jensen@mail.com"
        self.assertEqual(esperado, self.email.from_email)

    def test_contact_email_to(self):
        esperado = ['contato@eventif.com.br', 'marina.jensen@mail.com']
        self.assertEqual(esperado, self.email.to)

    def test_contact_email_message(self):
        contents = ('Marina Jensen', 'marina.jensen@mail.com', '53 91234-5678', 'Olá mundo!')
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)