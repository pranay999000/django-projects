from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from . models import Room, Message

import logging

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, room):
    user_name = request.GET.get('username')
    room_name = Room.objects.get(room_name=room)

    return render(request, 'room.html', { 'username': user_name, 'roomname': room_name })

def checkroom(request):
    room = request.POST['room_name']
    user = request.POST['user_name']

    room = room.replace(" ", "")
    room = room.lower()

    if Room.objects.filter(room_name=room).exists():
        return redirect('/' + room + '?username=' + user)
    else:
        room_new = Room.objects.create(room_name=room)
        room_new.save()
        return redirect('/' + room + '?username=' + user)

def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']

    logger = logging.getLogger(__name__)
    logger.error(room_id)

    message_new = Message.objects.create(text=message, user=username, room=room_id)
    message_new.save()

    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(room_name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({
        "messages": list(messages.values())
    })
