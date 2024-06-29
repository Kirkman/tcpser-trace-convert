import io
import os
import re
import argparse
import warnings
from argparse import RawTextHelpFormatter


def main(input_file=None, output_file=None):

	trace_re = re.compile(r'(.+?)\|(....)\|(.+?)\|(.+?)\|')

	in_text = ''
	out_text = ''

	with open(input_file, 'r') as f:
		in_text = f.read()

	lines = in_text.splitlines()

	for line in lines:
		if line.strip() == '':
			continue

		pieces = re.search(trace_re, line)
		if pieces:
			received_bytes = pieces[3]
			received_string = bytearray.fromhex(received_bytes).decode()

			out_text += received_string
			print(f'  {received_string}')

	with io.open(output_file, 'w', encoding='utf-8') as f:
		f.write(out_text)




if __name__ == "__main__":

	# CHECK FOR COMMAND LINE ARGUMENTS
	parser = argparse.ArgumentParser(
		description="""
This script will extract the bytes within tcpser\'s trace data and save them as a text file. Useful for capturing ANSI or other data sent by a BBS.
This script only works with trace data formatted like this:
	2024-06-29 13:07:44:123145390972928:TRACE:SR->|00b0|3a 57 3e 38 2c 37 38 2c 47 55 41 52 44 49 41 4e|:W>8,78,GUARDIAN|
	2024-06-29 13:07:44:123145390972928:TRACE:SR->|00c0|20 4f 46 20 46 4f 52 45 56 45 52 40 0d 0a 47 23| OF FOREVER@..G#|
(NOTE: To obtain clean trace data, run tcpser with the `-tS` and `-l0` flags, then save the terminal output to a text file.)
""",
		formatter_class=RawTextHelpFormatter,
	)

	parser.add_argument(
		'input',
		type=str,
		nargs='?',
		help='Filename and path for saved tcpser trace file. REQUIRED.'
	)

	parser.add_argument(
		'output',
		type=str,
		default='output.txt',
		nargs='?',
		help='Filename and path for output text file. Defaults to `./output.txt`.'
	)

	args = parser.parse_args()

	input_file = None
	if args.input:
		input_file = args.input

	output_file = None
	if args.output:
		output_file = args.output
	else:
		output_file = 'output.txt'

	main(
		input_file=input_file,
		output_file=output_file,
	)
