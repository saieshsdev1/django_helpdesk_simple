from django.test import TestCase

from .models import Ticket


class TicketModelTest(TestCase):
    def test_ticket_string(self):
        ticket = Ticket.objects.create(
            ticket_id='T1001',
            customer='Asha',
            issue='Cannot log in',
            priority='High',
        )
        self.assertEqual(str(ticket), 'T1001 - Asha')
