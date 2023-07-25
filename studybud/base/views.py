from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn React'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room_to_render = None
    for room in rooms:
        if room['id'] == int(pk):
            room_to_render = room
            break
    context = {'room': room_to_render}
    return render(request, 'base/room.html', context)
