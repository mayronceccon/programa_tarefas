# -*- coding: utf-8 -*-

import http.client
from xmlrpc.client import ServerProxy, ProtocolError, Transport

class ProxiedTransport(Transport):
    def set_proxy(self, proxy):
        self.proxy = proxy
    def make_connection(self, host):
        self.realhost = host
        h = http.client.HTTP(self.proxy)
        return h
    def send_request(self, connection, handler, request_body):
        connection.putrequest("POST", 'http://%s%s' % (self.realhost, handler))
    def send_host(self, connection, host):
        connection.putheader('Host', self.realhost)

p = ProxiedTransport()
proxy = ServerProxy("http://localhost/xml/server.php", transport=p)

try:
    result = proxy.tarefas.add(25, 30)
    print(result)
    pass

except ProtocolError as err:
    print("A protocol error occurred")
    print("URL: %s" % err.url)
    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)
    print("Error message: %s" % err.errmsg)