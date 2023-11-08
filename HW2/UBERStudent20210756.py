#!/usr/bin/python3

import datetime, calendar, sys

weekday_code = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}

input_file = sys.argv[1]
output_file = sys.argv[2]
data = {}

with open(input_file, 'r') as file:
	lines = file.readlines()
	for l in lines:
		inform = l.strip().split(',')
		num, date, vehicle, trip = inform
		date = datetime.datetime.strptime(date, '%m/%d/%Y')
		week = date.weekday()

		if num not in data:
			data[num] = {}
		if week not in data[num]:
			data[num][week] = {'vehicle': 0, 'trip': 0}

		data[num][week]['vehicle'] += int(vehicle)
		data[num][week]['trip'] += int(trip)

with open(output_file, 'w') as output:
	for num, day in data.items():
		for day, value in day.items():
			day_name = weekday_code[day]
			vehicle = value['vehicle']
			trip = value['trip']
			output_l = f"{num}, {day_name} {vehicle}, {trip}\n"
			output.write(output_l)
