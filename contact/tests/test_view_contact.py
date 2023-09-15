from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail

class ContactGetTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_contact_get(self):
        """GET /contato/ must return status_code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_contact_template(self):
        """Must use contact/contact_form.html as template"""
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')

    def test_form_contact_html(self):
        """HTML must contain input tags"""
        tags = (("<form", 1),
                ("<input", 5),
                ("<textarea", 1),
                ('type="text"', 2),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
                
    def test_form_contact_csrf(self):
        """Contact HTML must contain csrf"""
        self.assertContains(self.response,  "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have contact form"""
        form = self.response.context["form"]
        self.assertIsInstance(form, ContactForm)