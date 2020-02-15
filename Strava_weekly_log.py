#If this script ever stops working make sure the chrome version and webdrivers are up to date
#Align properly cause if not the script will not work properly
#Will need to check the Chrome version that the laptop is using

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import writer
import time

def get_Harris_run_mileage(url):
    driver.get(url)
    H_miles_ran = driver.find_elements_by_class_name('actual')[0].text
    time.sleep(1)
    if H_miles_ran is '':
        H_miles_ran = '0 mi'
        return (H_miles_ran[:-3])
    elif H_miles_ran.endswith("mi"):
        return H_miles_ran[:-3]
    else:
        return (H_miles_ran)

def get_Cooper_run_mileage(url):
    driver.get(url)
    C_miles_ran = driver.find_elements_by_class_name('actual')[0].text
    time.sleep(1)
    if C_miles_ran is '':
        C_miles_ran = '0 mi'
        return (C_miles_ran[:-3])
    elif C_miles_ran.endswith("mi"):
        return C_miles_ran[:-3]
    else:
        return (C_miles_ran)

username = 'username'
password = 'passsword'
#Username and Password information for Strava

Harris_Strava_url = 'https://www.strava.com/athletes/15522985?oq=ha'
Cooper_Strava_url = 'https://www.strava.com/athletes/15955087?oq=coop'

ellptical_time = float(input('Enter the minutes that you were on the ellptical here: '))
elliptical_mileage = round(((ellptical_time * 60) / (510)), 2)
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
harris_run_mileage = get_Harris_run_mileage(Harris_Strava_url)
cooper_run_mileage = get_Cooper_run_mileage(Cooper_Strava_url)

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
    csv_writer.writerow(['Running miles', 'Biking miles', 'Total miles', 'Harris mileage', 'Cooper mileage'])
    csv_writer.writerow([miles_ran, miles_biked, total_mileage, harris_run_mileage, cooper_run_mileage])
