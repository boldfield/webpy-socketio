#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       socketio_app.py
#
#       Copyright 2012 Di SONG <di@di-debian>
#       Copyright 2013 Brian Oldfield <brian@oldfield.io>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import web
from socketio import socketio_manage

from webpy_socketio.channels import SocketIOChannelProxy
from webpy_socketio.clients import client_start, client_end
from webpy_socketio.namespace import namespaces


class socketio(object):

    def GET(self):
        """Socket.IO handler - maintains the lifecycle of a Socket.IO
        request, sending the each of the events. Also handles
        adding/removing request/socket pairs to the CLIENTS dict
        which is used for sending on_finish events when the server
        stops.
        """
        context = {}
        socket = SocketIOChannelProxy(web.ctx.env["socketio"])
        request = web.ctx.env
        client_start(request, socket, context)
        socketio_manage(request, namespaces, request)
        client_end(request, socket, context)
        return ""


socketio_urls = ('/socket\.io/.*', socketio,)
