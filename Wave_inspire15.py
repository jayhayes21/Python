from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_shoe_price(url):
    driver.get(url)
    time.sleep(2)
    number = len(driver.find_elements_by_id('priceblock_ourprice'))
    shoe_size = driver.find_elements_by_class_name('a-dropdown-prompt')[0].text
    if number != 0 and shoe_size is '11.5':
        price_list.append(float(driver.find_elements_by_id('priceblock_ourprice')[0].text[1:]))



amazon_url1 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07CHTZ7LY/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
amazon_url2 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07CKJFBN5/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
amazon_url3 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07HRJ3HQR/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
amazon_url4 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07HRHQW9H/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
amazon_url5 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07CHV7B95/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
amazon_url6 = 'https://www.amazon.com/Mizuno-Mens-Inspire-Running-Teal-Dress/dp/B07CKJ6TKM/ref=sr_1_1?crid=1NP6MYQ13T6S7&dchild=1&keywords=wave%2Binspire%2B15%2Bmen&qid=1585569820&sprefix=wave%2Binsp%2Caps%2C163&sr=8-1&th=1&psc=1'
price_point = 70.50
price_list = []

chrome_driver_path = r"path/to/chromedriver"
options = Options()
options.headless = True
# options.headless = False
driver = webdriver.Chrome(chrome_driver_path, options=options)
get_shoe_price(amazon_url1)
get_shoe_price(amazon_url2)
get_shoe_price(amazon_url3)
get_shoe_price(amazon_url4)
get_shoe_price(amazon_url5)
get_shoe_price(amazon_url6)
driver.close()

for items in price_list:
    if items < price_point:
        print('Mizuno Wave Inspire are on sale for $' + str(items))

print('Script has finished executing.')
