import sys

from collect import (find_place)

def main():
	if sys.argv < 2:
		print "Usage: `python main.py <location>`"
	
	else:
		location = sys.argv[1]
		find_place(location)

if __name__ == "__main__":
	main()