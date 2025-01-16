from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):  # predefined hanlers
        print("Websocket Connected...",event)
        self.send({
            'type':  'websocket.accept'
        })
    # 'websocket_connect' handler is called when client initially opens a connection and is about to finish the websocket handshake.

    def websocket_receive(self,event):  # predefined hanlers
        print("Message Received...",event)
        print('Message is ',event['text'])
    # This handler is called when a data received from the client.

    def websocket_disconnect(self,event):  # predefined hanlers
        print("Websocket Disconnected...",event)
        raise StopConsumer()
    # This handler is called when either connection to the client is lost, either from the client closing the connection, or loss of the socket

class MyASyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):  # predefined hanlers
        print("Websocket Connected...",event)
        await self.send({
            'type':  'websocket.accept'
        })
    # 'websocket_connect' handler is called when client initially opens a connection and is about to finish the websocket handshake.

    async def websocket_receive(self,event):  # predefined hanlers
        print("Message Received...",event)
        print('Message is ',event['text'])
    # This handler is called when a data received from the client.

    async def websocket_disconnect(self,event):  # predefined hanlers
        print("Websocket Disconnected...",event)
        raise StopConsumer()
    # This handler is called when either connection to the client is lost, either from the client closing the connection, or loss of the socket
