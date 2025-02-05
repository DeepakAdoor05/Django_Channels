# Topic - Chat App with Dynamic Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import asyncio

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('WebSocket Connected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        self.group_name = self.scope['url_route']['kwargs']['Group_Name'] # Here we get the group name.
        print('Group Name...',self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
            )
        self.send({
            'type' : "websocket.accept",
            'text' : 'Hi from server'
        })

    def websocket_receive(self,event):
        print('Message Received from client...',event['text'])
        print('Type of Message Received from client...',type(event['text']))
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type' : 'chat.message',
                'message' : event['text']
            }
        )
    def chat_message(self,event):
        print('Event...',event)
        print('Actual Data...',event['message'])
        print('Type of Actual data...',type(event['message']))
        self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    def websocket_disconnect(self,event):
        print('WebSocket Disconnected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
            )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('WebSocket Connected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        self.group_name = self.scope['url_route']['kwargs']['Group_Name'] # Here we get the group name.
        print('Group Name...',self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
            )
        await self.send({
            'type' : "websocket.accept",
            'text' : 'Hi from server'
        })

    async def websocket_receive(self,event):
        print('Message Received from client...',event['text'])
        print('Type of Message Received from client...',type(event['text']))
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type' : 'chat.message',
                'message' : event['text']
            }
        )
    async def chat_message(self,event):
        print('Event...',event)
        print('Actual Data...',event['message'])
        print('Type of Actual data...',type(event['message']))
        await self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    async def websocket_disconnect(self,event):
        print('WebSocket Disconnected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        await self.channel_layer.group_discard(
            self.group_name,
             self.channel_name
        )
        raise StopConsumer()