from django.shortcuts import get_object_or_404, redirect, render

from .models import Ticket


def home(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'tickets/home.html', {'tickets': tickets})


def add_ticket(request):
    if request.method == 'POST':
        Ticket.objects.create(
            ticket_id=request.POST['ticket_id'],
            customer=request.POST['customer'],
            issue=request.POST['issue'],
            priority=request.POST['priority'],
        )
        return redirect('home')

    return render(request, 'tickets/add_ticket.html')


def close_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = 'Closed'
    ticket.save()
    return redirect('home')
