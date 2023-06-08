from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thedailystar.net/tech-startup"
path = "C:/Users/Shanto/Downloads/Programs/chromedriver_win32"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)