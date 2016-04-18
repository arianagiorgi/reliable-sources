import sys

from collect import (find_place)
from send import (send_to_google_drive)

def main():
	if sys.argv < 2:
		print "Usage: `python main.py <location>`"

	else:
		location = sys.argv[1]
		find_place(location)
		send_to_google_drive()

if __name__ == "__main__":
	main()
