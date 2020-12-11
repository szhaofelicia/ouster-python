import socket
import socketserver
import threading
from pprint import pprint


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print('The type of current server: {}'.format(self.server))
        print('Request sent to : {}'.format(self.request))
        print('Current client address: {}'.format(self.client_address))

        print('Threading list: {}'.format(threading.enumerate()))
        print('Current thread：{}'.format(threading.current_thread()))

localhost = socketserver.TCPServer(('127.0.0.1', 9000), Handler)
localhost.serve_forever()

# localhost.shutdown()

ethernet = socketserver.TCPServer(('192.168.0.141', 9000), Handler)
ethernet.serve_forever()
ethernet.shutdown()

# vpn = socketserver.TCPServer(('10.27.94.178', 9000), Handler)
# vpn.serve_forever()
# vpn.shutdown()


# udpserver = socketserver.UDPServer(('192.168.0.141', 7502), Handler)
# udpserver.serve_forever()
# udpserver.shutdown()


"""
The type of current server: <socketserver.TCPServer object at 0x7f7418720438>
Request sent to : <socket.socket fd=13, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 55724)>

Current client address: ('127.0.0.1', 55716)
Threading list: [<_MainThread(MainThread, started 140136788903680)>, <HistorySavingThread(IPythonHistorySavingThread, started 140136631916288)>]
Current thread：<_MainThread(MainThread, started 140136788903680)>


The type of current server: <socketserver.TCPServer object at 0x7f914c2d8908>
Request sent to : <socket.socket fd=15, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.0.141', 9000), raddr=('192.168.0.141', 40452)>
Current client address: ('192.168.0.141', 40452)
Threading list: [<_MainThread(MainThread, started 140262203434752)>, <HistorySavingThread(IPythonHistorySavingThread, started 140262046447360)>]
Current thread：<_MainThread(MainThread, started 140262203434752)>



"""