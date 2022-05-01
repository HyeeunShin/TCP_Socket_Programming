from socket import *
class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
            MSGLEN = 0

        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def RequestGET(self, msg):
        totalsent = 0

        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def ResponseGET(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def RequestPOST(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < len(msg):
            chunk = self.sock.recv(min(len(msg) - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

    def responsePOST(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < len(msg):
            chunk = self.sock.recv(min(len(msg) - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)