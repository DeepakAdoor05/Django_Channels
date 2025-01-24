# Topic - Chat App with static Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions  import StopConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('WebSocket Connected...',event)
        self.send({
            'type' : "websocket.accept",
        })

    def websocket_receive(self,event):
        print('Message Received from client...',event)

    def websocket_disconnect(self,event):
        print('WebSocket Disconnected...',event)
        raise StopConsumer()