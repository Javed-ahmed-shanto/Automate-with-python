"""
The Program for web scrapping from any website using python. please install latest chrome driver and google chrome and also intall pandas and selenium

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thedailystar.net/tech-startup"
path = "C:/Users/Shanto/Downloads/Programs/chromedriver_win32"


# Headless mode
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="card-content pt-20 pb-20 pr-20"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by = "xpath", value = './h3').text
    titles.append(title)

    subtitle = container.find_element(by = "xpath", value = './p').text
    subtitles.append(subtitle)
    link = container.find_element(by="xpath", value='./h3/a').get_attribute("href")
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()