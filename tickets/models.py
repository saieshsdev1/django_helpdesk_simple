from django.db import models


class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    ticket_id = models.CharField(max_length=20, unique=True)
    customer = models.CharField(max_length=100)
    issue = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ticket_id} - {self.customer}'
