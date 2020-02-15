import requests
from datetime import datetime,date
import time
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dateutil import tz

class Trackerinfo():
     index = []
     running_miles = []
     running_pace = []
     local_date = []
     utc_date = []


biking_events = 0
offset = 3

username = 'username'
password = 'password'

path_to_log = r'path to running log'
chrome_driver_path = r"path to chromedriver"
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_driver_path, options=options)

driver.get('https://www.strava.com/dashboard?feed_type=my_activity')
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('password').send_keys(Keys.RETURN)
time.sleep(2)

old_run = str(driver.find_elements_by_xpath('//b[@class=\'stat-text\']')[offset].get_attribute('innerHTML')[0:4])
old_pace = str(driver.find_elements_by_xpath('//b[@class=\'stat-text\']')[offset+1].get_attribute('innerHTML')[0:7])
strava_csv_date = str(driver.find_elements_by_xpath('//time[@class=\'timestamp\']')[biking_events + 1].get_attribute('outerHTML'))[34:57]
strava_run_time = str(driver.find_elements_by_xpath('//time[@class=\'timestamp\']')[biking_events + 1].get_attribute('outerHTML'))[34:44]
driver.close()

old_pace = old_pace[0:4] + ' /mi'
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
utc = datetime.strptime(strava_csv_date[:-4], '%Y-%m-%d %H:%M:%S')
utc = utc.replace(tzinfo=from_zone)
central = str(utc.astimezone(to_zone))

Year = central[0:4]
Month = central[5:7]
Day = central[8:10]
modified_date = Month + '/' + Day + '/' + Year

my_object = Trackerinfo()

line_count = 0
with open(path_to_log) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        line_count += 1
        my_object.index.append(row[0])
        my_object.running_miles.append(row[1])
        my_object.running_pace.append(row[2])
        my_object.local_date.append(row[3])
        my_object.utc_date.append(row[4])

with open(path_to_log, 'w', newline= '') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in range(0, line_count):
        csv_writer.writerow([my_object.index[row],my_object.running_miles[row],my_object.running_pace[row],my_object.local_date[row],my_object.utc_date[row]])
    csv_writer.writerow([line_count,old_run,old_pace,modified_date,strava_csv_date])
