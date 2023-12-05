from datetime import datetime
from django.test import TestCase
from contact.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.data = Contact(
            name='Marina Jensen',
            email='marina.jensen@mail.com',
            phone='53 91234-5678',
            message='Olá mundo!')
        self.data.save()

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.data.created_at, datetime)

    def test_replied_default(self):
        self.assertFalse(self.data.replied)

    def test_string(self):
        self.assertEqual(str(self.data), 'Marina Jensen')
