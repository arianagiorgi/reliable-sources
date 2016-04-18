import sys

from collect import (find_place)
from send import (send_to_google_drive)

def main():
	if len(sys.argv) < 2:
		print "Usage: `python main.py <location> <optional: keyword>`"

	else:
		location = sys.argv[1]
		
		#optional keyword setting
		if len(sys.argv) == 3:
			keyword = sys.argv[2]
			find_place(location, keyword)
		else:
			find_place(location)
			
		send_to_google_drive()

if __name__ == "__main__":
	main()
