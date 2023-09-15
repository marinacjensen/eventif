from django.test import TestCase
from contact.forms import ContactForm

class contactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()
    def test_form_has_fields(self):
        self.assertSequenceEqual(['name', 'email', 'phone', 'message'], list(self.form.fields))