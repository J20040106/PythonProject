from selenium import webdriver
URL = 'https://www.selenium.dev/ko/documentation/'

driver = webdriver.Chrome() # "./chromedriver.exe"
driver.get(url=URL)