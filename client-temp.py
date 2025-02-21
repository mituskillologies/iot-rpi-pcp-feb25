import socket
s = socket.socket()
s.connect(('10.40.2.162',1234))
print('Temperature from server:', s.recv(20))
s.close()
