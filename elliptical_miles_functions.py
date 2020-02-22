from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def get_elliptical_miles(file_name):
    file = open(file_name, 'r+')
    elliptical_miles = file.read()
    if elliptical_miles is '':
        file.close()
        return elliptical_miles
    else:
        elliptical_miles = float(elliptical_miles)
        file.close()
        return elliptical_miles


def set_elliptical_miles(time, file_name):
    writable_time = str(time)
    file = open(file_name, 'w+')
    file.write(writable_time)
    file.close()

def daily_bike_entry(bike_miles, minutes):
    username = 'username'
    password = 'passsword'
    # Username and Password information for Strava

    chrome_driver_path = r"path to chromedriver"

    options = Options()
    # options.headless = False
    options.headless = True
    driver = webdriver.Chrome(chrome_driver_path, options=options)

    driver.get('https://www.strava.com/dashboard')
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('password').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.get('https://www.strava.com/upload/manual')
    driver.find_element_by_id('activity_distance').send_keys(bike_miles)
    driver.find_elements_by_class_name('selection')[10].click()
    time.sleep(1)
    driver.find_elements_by_tag_name('li')[111].click()
    driver.find_element_by_id('activity_elapsed_time_minutes').clear()
    driver.find_element_by_id('activity_elapsed_time_minutes').send_keys(minutes)
    driver.find_element_by_id('activity_elapsed_time_hours').clear()
    driver.find_element_by_id('activity_elapsed_time_hours').send_keys('00')
    driver.find_elements_by_class_name('btn-primary')[1].click()
    driver.close()

def clear_file_contents(filename):
    file = open(filename, 'w+')
    file.close()