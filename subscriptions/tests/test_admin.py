from django.test import TestCase
from subscriptions.admin import SubscriptionModelAdmin, Subscription, admin

from unittest.mock import Mock


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Marina Jensen',
            cpf='12345678901',
            email='marina.jensen@mail.com',
            phone='53 91234-5678'
        )

        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        self.call_action()
        self.mock.assert_called_once_with(
            None, '1 inscrição foi marcada como paga')

    def call_action(self):
        queryset = Subscription.objects.all()

        self.mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user

        SubscriptionModelAdmin.message_user = self.mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user
