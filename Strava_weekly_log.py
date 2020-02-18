#If this script ever stops working make sure the chrome version and webdrivers are up to date
#Align properly cause if not the script will not work properly
#Will need to check the Chrome version that the laptop is using

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import writer
import time
from elliptical_miles_functions import get_elliptical_miles, clear_file_contents

def get_runners_mileage(url):
    driver.get(url)
    miles_ran = driver.find_elements_by_class_name('actual')[0].text
    time.sleep(1)
    if miles_ran is '':
        miles_ran = '0 mi'
        return (miles_ran[:-3])
    elif miles_ran.endswith("mi"):
        return miles_ran[:-3]
    else:
        return (miles_ran)


username = 'username'
password = 'passsword'
#Username and Password information for Strava

elliptical_tracker_file = 'elliptical_miles.txt'

Harris_Strava_url = 'https://www.strava.com/athletes/15522985?oq=ha'
Cooper_Strava_url = 'https://www.strava.com/athletes/15955087?oq=coop'
Brain_Wang_url = 'https://www.strava.com/athletes/27576319?oq=bri'

ellptical_time = get_elliptical_miles(elliptical_tracker_file)
elliptical_mileage = round(((ellptical_time * 60) / (510)), 2)
clear_file_contents(elliptical_tracker_file)
#Calculating elliptical mileage assuming a pace of 8:30 per mile

path_to_log = r'path to posts.csv'
chrome_driver_path = r"path to chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

driver.get('https://www.strava.com/dashboard')
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('password').send_keys(Keys.RETURN)
time.sleep(2)

miles_ran = driver.find_elements_by_class_name('actual')[0].text
harris_run_mileage = get_runners_mileage(Harris_Strava_url)
cooper_run_mileage = get_runners_mileage(Cooper_Strava_url)
brian_run_mileage = get_runners_mileage(Brain_Wang_url)

driver.get('https://www.strava.com/dashboard')
miles_ran = round(float(miles_ran[:-3]) + elliptical_mileage, 2)
driver.find_element_by_class_name('icon-ride').click()
miles_biked = driver.find_elements_by_class_name('actual')[1].text
driver.close()
miles_biked = float(miles_biked[:-3])
total_mileage = miles_ran + miles_biked

# want to write to rows 5, 6, 7 in my excel file
with open(path_to_log, 'w', newline = '') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['Running miles', 'Biking miles', 'Total miles', 'Harris mileage', 'Brian mileage', 'Cooper mileage'])
    csv_writer.writerow([miles_ran, miles_biked, total_mileage, harris_run_mileage, brian_run_mileage, cooper_run_mileage])
