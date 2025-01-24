# Topic - Chat App with static Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions  import StopConsumer
from asgiref.sync import async_to_sync
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('WebSocket Connected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        async_to_sync(self.channel_layer.group_add)(
            'programmers',
            self.channel_name
            )
        self.send({
            'type' : "websocket.accept",
        })

    def websocket_receive(self,event):
        print('Message Received from client...',event['text'])
        print('Type of Message Received from client...',type(event['text']))

    def websocket_disconnect(self,event):
        print('WebSocket Disconnected...',event)
        print("Channel Layer",self.channel_layer)   # gets the default channel_layer from a project.
        print("Channel Name",self.channel_name)     # get channel name.
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
            )
        raise StopConsumer()