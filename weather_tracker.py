import requests
import json
import datetime
from datetime import datetime, date
import calendar
import time
import csv
from dateutil import tz

user_define_index = input('Enter the index number of the run you would like to see the weather information from: ')
interval = int(input('Enter the interval in minutes you want to see the run for: '))
print('\n')
length_of_run = 0
loop_duration = 6
input_time = ''

path_to_log = r'path to running log'

with open(path_to_log) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if(row[0] == user_define_index):
            length_of_run = row[1]
            pace = row[2]
            loop_duration = int((float(length_of_run)*float(pace[0])+(float(length_of_run)*(float(pace[2:4])/60))))
            input_time = row[4]
            break

Year = int(input_time[0:4])
Month = int(input_time[6])
Day = int(input_time[8:10])
Hour = int(input_time[11:13])
Minute = int(input_time[14:16])
Seconds = int(input_time[17:19])


Milford_coordinates = '39.17534,-84.29438'
Cincinnati_coordinates = '39.0943,-84.2724'

for x in range(0, loop_duration+1, interval):
    formatted_date = datetime(Year, Month, Day, Hour, Minute, Seconds)
    timestamp = int(calendar.timegm(formatted_date.timetuple()))
    response = requests.get('https://api.darksky.net/forecast/enter personal key here/enter your coordinates here,'+str(timestamp)+'?exclude=daily,flags')
    data = response.json()

    Weather_description = data['currently']['summary']
    Time = data['currently']['time']
    Weather_temperature = data['currently']['temperature']
    Weather_humidity = data['currently']['humidity']

    utc_time = str(datetime.utcfromtimestamp((Time)))
    utc_hour = int(utc_time[11:13])
    local_day = int(utc_time[8:10])
    local_hour = utc_hour-4
    if(local_hour < 0):
        local_hour += 24
    if local_day < 10:
        local_time = utc_time[0:8]+ '0' +str(local_day)+' '+str(local_hour)+utc_time[13:]
    else:
        local_time = utc_time[0:8] + str(local_day)+' '+ str(local_hour) + utc_time[13:]
    timestamp += (60*interval)
    Minute += interval
    if(Minute >= 60):
        Minute = (Minute % 60)
        Hour += 1
    if(Hour > 23):
        Hour -= 24
        Day += 1
    if(Hour < 4):
        utc_hour = (Hour+24)
        local_day -= 1
    day = datetime.strptime(local_time[0:10], '%Y-%m-%d').strftime('%B %d, %Y')
    my_time = datetime.strptime(local_time[11:], '%H:%M:%S').strftime('%I:%M:%S %p')
    print('On '+ day + ' it was '+Weather_description + ' at ' + my_time+'. It was ' + str(Weather_temperature) + ' degrees outside with a humidity of ' + str(Weather_humidity))