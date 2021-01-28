import os
import sys
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
def google(user, req_ur, seng):
	try:
		print("[+] Enumerating person in almost 10 Social Medias...")	
		first = urlopen('https://www.facebook.com/{}'.format(user))
		zig1 = requests.get('https://www.facebook.com/{}'.format(user))
		print("[+] Enumeration completed! User exists on Facebook! ")
		second = urlopen('https://www.instagram.com/{}/?hl=en'.format(user))
		print("[+] Enumeration Completed! User exists on Instagram!")
		third = urlopen('https://www.tiktok.com/@{}?lang=en'.format(user))
		print("[+] Enumeration Completed! User exists on TikTok!")
		fourth = urlopen("https://www.youtube.com/{}".format(user))
		print("[+] Enumeration Completed! User exists on YouTube!")
		fifth = urlopen("https://{}.blogspot.com".format(user))
		print("[+] Enumeration Completed! User exists on Blogspot!")
		sixth = urlopen("https://plus.google.com/{}/posts".format(user))
		print("[+] Enumeraiton Completed! User exists on Google+")
		seventh = urlopen("https://www.reddit.com/user/{}".format(user))
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		pass 
def main():
	try:
		user = sys.argv[1]
		req_ur = sys.argv[2]
		seng = sys.argv[3]
		if seng == 'google':
			if req_ur == 'request':
				google(user, req_ur, seng)
			if req_ur == 'urllib':
				google(user, req_ur, seng)
			else:
				print("Unrecognized search engine!")
				sys.exit(1)
		if seng == 'bing':
			if req_ur == 'request':
				bing(user, req_ur, seng)
			if req_ur == 'urllib':
				bing(user, req_ur, seng)
			else:
				print("Unrecognized search engine!")
				sys.exit(1)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <user> <request/urllib> <search engine>")
main()
