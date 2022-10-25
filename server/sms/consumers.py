import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from .models import Sms


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        app_name = self.scope['url_route']['kwargs']['app']
        self.room_group_name = app_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        # Check if app name existed in DB
        app = User.objects.filter(username=app_name).first()
        if not app:
            self.close()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'msg': 'You are now connected!',
            "phone": ""
        }))

    def receive(self, text_data=None):
        app_name = self.scope['url_route']['kwargs']['app']
        text_data_json = json.loads(text_data)
        phone = text_data_json['phone']
        msg = text_data_json['msg']
        
        async_to_sync(self.channel_layer.group_send)(
            app_name,
            {
                'type': 'send_to_gui',
                'phone': phone,
                'msg': msg,
                'app': app_name
            }
        )

    def send_to_gui(self, event):
        phone = event["phone"]
        msg = event["msg"]

        self.send(text_data=json.dumps({
            'type': 'send_to_gui',
            'phone': phone,
            "msg": msg
        }))