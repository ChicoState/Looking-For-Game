# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . import models
from django.utils import timezone

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        # load previous messages

        print("Room name is")
        print(self.room_name)

        # == LEGACY REFERENCE == artist_obj = models.Artist.objects.get(artist_id=int(self.room_name))
        #   messages_list = artist_obj.messagemodel_set.all()
        group_obj = models.Group.objects.get(group_number=int(self.room_name))
        messages_list = group_obj.messagemodel_set.all()
        messages = sorted(messages_list, key=lambda x: x.time)
        #messages = models.MessageModel().recent_messages()
        if len(messages) != 0:
            print("Loading Messages")
            for message in messages:
                my_message = message.time + "| " + message.sender + ": " + message.message_text
                self.messages_output(my_message)


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def create_message(self, myMessage):
        pass

    # Receive message from WebSocket

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #message_send = text_data_json['sender'] + ": " + text_data_json['message']


        message = models.MessageModel.objects.create(
            sender = text_data_json['sender'],
            message_text = text_data_json['message'],
            time = (str)(timezone.now())[0:19],
            group = models.Group.objects.get(group_number=text_data_json['option'])
        )


        message_send = str(message.time) + "| " + message.sender + ": " + message.message_text
        #message_send = message.sender + ": " + message.message_text

        # one new message
        self.messages_output(message_send)

    def messages_output(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
