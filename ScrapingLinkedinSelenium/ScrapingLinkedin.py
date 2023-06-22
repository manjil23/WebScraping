from sqlite3 import Date
import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path=r"C:\Users\mlpradhan\source\repos\Linkedin\ScrapingLinkedinSelenium\chromedriver.exe")
browser.get("https:www.linkedin.com")

username = browser.find_element_by_id("session_key")
username.send_keys("projectecommercetest@gmail.com")
password = browser.find_element_by_id("session_password")
password.send_keys("Iam@job123")

login_button = browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

browser.get("https://www.linkedin.com/jobs/search/?f_JT=F&f_TPR=r86400&f_WT=2%2C3&keywords=c%23")

# get a list of all the listings elements's in the side bar
list_items = browser.find_elements_by_class_name("occludable-update")
# scrolls a single page:
# Tuple1=()
# x=list(Tuple1)
PositionOpen= []
CompanyHiring =[]
Location =[]
JobType =[]

for job in list_items:  
    # executes JavaScript to scroll the div into view
    
    browser.execute_script("arguments[0].scrollIntoView();", job)
    # job.click()
    # time.sleep(3)
    # get info:
    [position, company, location,jobtype] = job.text.split('\n')[:4]
    PositionOpen.append(position)
    CompanyHiring.append(company)
    Location.append(location)
    JobType.append(jobtype)
    # Tuple1=(position, company, location,JobType)
    # x.append(Tuple1)
    # Tuple1 = tuple(x)
    # details = browser.find_element_by_id("job-details").text
    # print(job.text)
# print(Tuple1)
# print()
# print(len(Tuple1))

Col = ["PositioinOpen","CompanyHiring","Location","JobType"]
df = pd.DataFrame({"PositioinOpen":PositionOpen, "CompanyHiring":CompanyHiring,"Location":Location,"JobType":JobType })
print(df.head())
df.to_excel("Linkedin Automation.xlsx")
