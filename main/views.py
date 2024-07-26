from django.shortcuts import render
from .models import Service, Client, BoardMember

def home(request):
    return render(request, 'main/home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'main/clients.html', {'clients': clients})

def board(request):
    board_members = BoardMember.objects.all()
    return render(request, 'main/board.html', {'board_members': board_members})
