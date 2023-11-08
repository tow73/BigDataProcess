#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as file:
	lines = file.readlines()

count = {}

for l in lines:
	sep = l.split('::')
	genre = sep[2].split('|')
	for g in genre:
		g = g.rstrip('\n')
		if g in count:
			count[g] += 1
		else:
			count[g] = 1

with open(output_file, 'w') as output:
	for g, c in count.items():
		output.write(f"{g} {c}\n")
