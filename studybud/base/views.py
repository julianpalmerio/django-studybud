from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn React'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render(request, 'base/room.html')
