from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin

from unittest.mock import Mock


class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='Marina Jensen',
            email='marina.jensen@mail.com',
            phone='53 91234-5678',
            message = 'Olá mundo!'
        )

        self.model_admin = ContactModelAdmin(Contact, admin.site)

    def test_has_action(self):
        self.assertIn('reply_check', self.model_admin.actions)

    def test_mark_all(self):
        self.call_action()
        self.assertEqual(1, Contact.objects.filter(replied=True).count())

    def test_message(self):
        self.call_action()
        self.mock.assert_called_once_with(
            None, '1 mensagem foi retornada.')

    def call_action(self):
        queryset = Contact.objects.all()

        self.mock = Mock()
        old_message_user = ContactModelAdmin.message_user

        ContactModelAdmin.message_user = self.mock

        self.model_admin.reply_check(None, queryset)

        ContactModelAdmin.message_user = old_message_user
