from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.keys import Keys
import time

def send_myself_email():
    email = 'Enter email name here'
    password = 'Enter password here'
    send_to_email = 'Where are you sending the email to'
    subject = 'Email Subject'
    message = 'Email Body'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)

jack_rabbit_url = 'https://www.jackrabbit.com/brands/mizuno/wave-inspire.html'
price_point = 67.50

chrome_driver_path = r"path to chromedriver"
options = Options()
options.headless = True
# options.headless = False
driver = webdriver.Chrome(chrome_driver_path, options=options)
driver.get(jack_rabbit_url)
time.sleep(2)
driver.find_elements_by_class_name('bx-button')[1].click()

for items in driver.find_elements_by_class_name('price'):
    if items.text is not '' and (len(items.text[1:]) < 6):
        jack_rabbit_price = float(items.text[1:])
        if jack_rabbit_price < price_point:
            #If the shoes are below the price point I will send myself an email
            send_myself_email()
driver.close()