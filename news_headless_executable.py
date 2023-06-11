"""
The Program for web scrapping from any website using python. please install latest chrome driver and google chrome and also intall pandas and selenium
this is headless mode. so the borwser will not open and everything will be done in background
this is an executable file. so before running this isntall pyinstaller. then run this code : python pyinstaller --onefile your_code_name.py 
after that you will find your executable file and the csv file in the dist folder
if you want to use this executable file everyday at your preferable time you can use crontab. to use cron crontab goto the terminal and write : "crontab -e"
this will open the crontab. for selecting the time of your choice you can use crontab guru website. for my case i used following commands.
09*** "(insert mode)path of the program(without quaotation)" (wq quit) 
for varifying use this command on the terminal"crontab -l"
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys



application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_date_year = now.strftime("%m%d%Y ") # MMDDYYYY

website = "https://www.thedailystar.net/tech-startup"
path = "C:/Users/Shanto/Downloads/Programs/chromedriver_win32"


# Headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
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
file_name = f'headline-{month_date_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()
