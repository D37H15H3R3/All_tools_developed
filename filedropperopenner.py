import os
import sys
def main_(word):
	with open(word, 'r') as file:
		for lines in file:
			words = lines.strip()
			x = "start chrome " + words
			os.system(x)
			pass 
def main():
	try:
		word = sys.argv[1]
		main_(word)
	except IndexError:
		print("\nUsage: ")
		print("python3 {} <list with sites> ")
		sys.exit(1)
main()
