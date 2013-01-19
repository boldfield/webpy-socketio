import sys

from socketio.namespace import BaseNamespace

from webpy_socketio.utils import format_log
from webpy_socketio import events


namespaces = {}


def add_namespace(endpoint, namespace):
    global namespaces
    namespaces[endpoint] = namespace


class GlobalNamespace(BaseNamespace):

    def __getattr__(self, name):
        if name.startswith('on_'):
            return self.handle
        return object.__getattribute__(self, name)

    def recv_message(self, packet):
        """Hanled messages sent with the socket.send() method.
        """
        return self.handle(packet)

    def recv_disconnect(self):
        """Called when client forces disconnect.
        """
        events.on_disconnect.send(self.request, self.socket, self.environ)

    def recv_connect(self):
        """Called when client connects.
        """
        events.on_connect.send(self.request, self.socket, self.environ)

    def handle(self, packet):
        """Handle an incoming packet on this socket.

        Event:
            {'endpoint': u'', 'type': 'event', 'name': u'hi', 'args': [{u'hello': u'world'}]}
        Message:
            {'data': u'hi', 'endpoint': u'', 'type': 'message'}
        """
        try:
            endpoint = packet['endpoint']
            channel = None
            type = packet['type']
            if type == 'event':
                channel = packet['name']
                message = packet['args']
                events.on_event.send(self.request, self.socket, self.environ, channel, endpoint, message)
            elif type == 'message':
                message = packet['data']
                events.on_message.send(self.request, self.socket, self.environ, None, endpoint, message)
            else:
                # TODO :: Determine if there are other types we might see here.
                # TODO :: Client side connect/disconnect handled by
                # TODO :: recv_connect() and recv_disconnect() respectively.
                pass
            log_message = format_log(self.request, type, message)
            if log_message:
                #self.socket.handler.server.log.write(log_message)
                pass
        except Exception, exception:
            from traceback import print_exc
            print_exc()
            events.on_error.send(self.request, self.socket, self.environ, channel, exception)
