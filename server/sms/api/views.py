import asyncio
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import SmsSerializer, UserSerializer
import websockets
import json


async def send_sms(request, host, app):
    url = "ws://"+host+"/ws/sms-server/"+app
    try:
        async with websockets.connect(url) as websocket:
            event = {"phone": request.data["phone"], "msg": request.data["msg"]}
            await websocket.send(json.dumps(event))
            return True
    except:
        return False


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    host = request.get_host()
    app_name = request.data["app"]
    if len(request.data["phone"]) != 12:
        return Response({"success": False, "message": "Phone must be 12 characters"}, status=status.HTTP_400_BAD_REQUEST)
    if not request.data["phone"].startswith('+9936'):
        return Response({"success": False, "message": "Incorrect phone number"}, status=status.HTTP_400_BAD_REQUEST)
    if request.data["phone"][5] not in "012345":
        return Response({"success": False, "message": "Incorrect phone number"}, status=status.HTTP_400_BAD_REQUEST)
    if len(request.data["msg"]) < 3:
        return Response({"success": False, "message": "Message must be at least 3 characters"}, status=status.HTTP_400_BAD_REQUEST)
    if app_name != request.user.username:
        return Response({"success": False, "message": "Incorrect app name!"}, status=status.HTTP_400_BAD_REQUEST)
    sms = SmsSerializer(data=request.data)
    if sms.is_valid():
        sms.save()
        ws_connection = asyncio.run(send_sms(request, host, app_name))
        if ws_connection:
            return Response({"success": True, "message": "Sent successfully!"})
        else:
            return Response({"success": False, "message": "WS Connection error"})
    else:
        return Response({"success": False, "message": "Data invalid!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    serializer = UserSerializer(request.user, many=False)
    return Response(serializer.data)