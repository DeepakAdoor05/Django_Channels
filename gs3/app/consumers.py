from channels.consumer import SyncConsumer,AsyncConsumer
class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):  # predefined hanlers
        print("Websocket Connected...",event)
    # 'websocket_connect' handler is called when client initially opens a connection and is about to finish the websocket handshake.

    def websocket_recieve(self,event):  # predefined hanlers
        print("Message Recieved...",event)
    # This handler is called when a data received from the client.

    def websocket_disconnect(self,event):  # predefined hanlers
        print("Websocket Disconnected...",event)
    # This handler is called when either connection to the client is lost, either from the client closing the connection, or loss of the socket

class MyASyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):  # predefined hanlers
        print("Websocket Connected...",event)
    # 'websocket_connect' handler is called when client initially opens a connection and is about to finish the websocket handshake.

    async def websocket_recieve(self,event):  # predefined hanlers
        print("Message Recieved...",event)
    # This handler is called when a data received from the client.

    async def websocket_disconnect(self,event):  # predefined hanlers
        print("Websocket Disconnected...",event)
    # This handler is called when either connection to the client is lost, either from the client closing the connection, or loss of the socket
