from selenium import webdriver
from time import sleep

driver_path = './chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

url = 'https://www.google.com/'
driver.get(url)