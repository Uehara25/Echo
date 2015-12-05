# -*- coding:utf-8 -*-

import asyncore

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8000)
        if data:
            self.send(data)


class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print("Incoming connection from {}".format(repr(addr)))
        handler = EchoHandler(scok)

server = EchoServer('localhost', 8000)
asyncore.loop()
