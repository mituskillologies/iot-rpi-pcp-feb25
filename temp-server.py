import Adafruit_DHT as dht
import socket
s = socket.socket()
s.bind(('10.40.2.162',1234))    # RPi IP-Address
s.listen(5)
while True:
	print('Waiting for client request....')
	c, addr = s.accept()
	print('Got Connection From', addr)
	hum, temp = dht.read_retry(11,4)
	c.send(str(temp).encode('utf-8'))
	c.close()
