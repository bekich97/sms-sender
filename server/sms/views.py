from django.shortcuts import render
from django.http import HttpResponse
from .consumers import ChatConsumer
import socket
import asyncio
import websockets
import json
from .models import Sms

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')


async def handler(websocket):
    event = {"message": "Hello From Python"}
    await websocket.send(json.dumps(event))


async def send_sms(request):
    url = "ws://127.0.0.1:5005/ws/sms-server/main"
    async with websockets.connect(url) as websocket:
        event = {"message": "Hello From Python"}
        await websocket.send(json.dumps(event))


async def my_post(request):
    await send_sms(request)
    return HttpResponse("Hi")


def clear(request):
    sms = Sms.objects.all()
    for s in sms:
        s.delete()
    return HttpResponse("Done")