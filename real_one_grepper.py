import os
import sys
import time
def grep(file, filename, ext):
	print("[+] Grepping...")
	with open(file, 'r') as filez:
		for lines in filez:
			try:
				wordie = lines.strip()
				print("Using word -  {}".format(wordie))
				cut = wordie[-10:]
				jump = '@yahoo.com'
				if jump in wordie:
					print("There is @yahoo, hold up!")
					zarrr = wordie.replace('@yahoo.com:','')
					cutz = zarrr[-7:]
					zarrr = wordie.replace('@verizon.net', '')
					zarrr = wordie.replace('@abv.bg', '')
					zarrr = wordie.replace('@hotmail.com', '')
					zarrr = wordie.replace('@', '')
					zarrr = wordie.replace(':', '')
					zarrr = wordie.replace('.', '')
					zarrr = wordie.replace('om.:','')
					zarrr = wordie.replace('a:', '')
					zarrr = wordie.replace('b:', '')
					zarrr = wordie.replace('c:', '')
					zarrr = wordie.replace('d:', '')
					zarrr = wordie.replace('e:', '')
					zarrr = wordie.replace('f:', '')
					zarrr = wordie.replace('g:', '')
					zarrr = wordie.replace('h:', '')
					zarrr = wordie.replace('i:', '')
					zarrr = wordie.replace('j:', '')
					zarrr = wordie.replace('k:', '')
					zarrr = wordie.replace('l:', '')
					zarrr = wordie.replace('m:', '')
					zarrr = wordie.replace('n:', '')
					zarrr = wordie.replace('o:', '')
					zarrr = wordie.replace('p:', '')
					zarrr = wordie.replace('q:', '')
					zarrr = wordie.replace('r:', '')
					zarrr = wordie.replace('s:', '')
					zarrr = wordie.replace('t:', '')
					zarrr = wordie.replace('u:', '')
					zarrr = wordie.replace('v:', '')
					zarrr = wordie.replace('w:', '')
					zarrr = wordie.replace('x:', '')
					zarrr = wordie.replace('y:', '')
					zarrr = wordie.replace('z:', '')
					zarrr = wordie.replace(':', '')
					zarrr = wordie.replace('com', '')
					zarrr = wordie.replace('com', ' ')
					zarrr = wordie.replace('om', '')
					zarrr = wordie.replace('.c:', '')
					zarrr = wordie.replace('c:', '')
					print("Word is - {}".format(cutz))
					z = filename + ext
					file = open(z, 'a')
					file.write("\n" + cutz)
			except KeyboardInterrupt:
				print("Closing file..[-]")
				sys.exit()
			except UnicodeDecodeError:
				pass 
def main():
	try:
		file = sys.argv[1]
		filename = sys.argv[2]
		ext = sys.argv[3]
		grep(file, filename, ext)
	except IndexError:
		print("\nUsage: ")
		print("python3 {}  <file>  <filename> <ext> ".format(sys.argv[0]))
		print("\nExample: python3 {} rockyouuemails.txt  lol .txt".format(sys.argv[0]))
		sys.exit()
main()
#python3 grep_me_in_the_ass.py C:\Users\Ruslan\Documents\email_access\100.txt