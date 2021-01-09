
"""
This program changes the time of subtitle files. It's a feature called syncronize subtitle in some video players.
It read the input filename, output filename(optional) and time(in seconds) respectively from the command line.
If filename has space, wrap it in apostrophe

Example:
	python sync_subtitle movie.srt result.srt -20    				# Speed up subtitle in movie.srt by 20 seconds and save to result.srt
	python sync_subtitle 'movie name year format.srt' 3.45   		# Delay subtitle in movie.srt by 3.45 seconds and save to movie.srt
"""

import re
from datetime import datetime, timedelta
import sys

def change_time(matchobj):
	time = datetime.strptime(matchobj.group(), "%X,%f")
	new_time = time+timedelta(seconds=seconds)
	result = new_time.strftime("%X,%f")[:-3] # %f is in microseconds. [-3] removes the last 3 digits and makes it milliseconds
	return result

def main():
	with open(input_filename) as input_file:
		string = input_file.read()

	pattern = r"\d{2}:\d{2}:\d{2},\d{3}"
	new_string = re.sub(pattern, change_time, string)
	
	with open(output_filename, 'w') as output_file:
		output_file.write(new_string)

if __name__ == '__main__':
	input_filename = sys.argv[1]
	if len(sys.argv)>3:
		output_filename = sys.argv[2]
		seconds = float(sys.argv[3])
	else:
		output_filename = input_filename
		seconds = float(sys.argv[2])

	main()