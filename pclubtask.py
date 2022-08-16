import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


Technologies = []
Topics = []
Brief_Description = []
Links = []


# from selenium.webdriver.support.select import Select
website='https://summerofcode.withgoogle.com/programs/2022/organizations'
path = 'C:\\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.maximize_window()
driver.get(website)
time.sleep(5)

parent_window1 = driver.current_window_handle

# drop down menu selection
drop_down = driver.find_element(By.XPATH, '//div[@class="mat-form-field-flex ng-tns-c87-2"]')
driver.execute_script("arguments[0].click();", drop_down)
time.sleep(2)
drop_all = driver.find_element(By.XPATH, '//mat-option[@id="mat-option-3"]')
driver.execute_script("arguments[0].click();", drop_all)
time.sleep(2)

#selecting and itteratiing over all organisation 1-100
organisations1 = driver.find_elements('xpath','//div[@class="info"]')

for organisation in organisations1:
    print(organisation.text)
    driver.execute_script("arguments[0].click();", organisation)

    #handling new window and itterating over current two windows
    child_windows = driver.window_handles
    for child in child_windows:
        #if new window is opened switch to new window
        if parent_window1!=child:
            driver.switch_to.window(child)
            time.sleep(5)
            #print the required data from this window
            data1 = driver.find_element('xpath','//div[@class="tech__content"]')
            data2 = driver.find_element('xpath','//div[@class="topics__content"]')
            data3 = driver.find_element('xpath','//div[@class="bd"]')
            data4 = driver.find_element('xpath','//a[@class="link"]')

            Technologies.append(data1)
            Topics.append(data2)
            Brief_Description.append(data3)
            Links.append(data4)

            print("Technologies - ",data1.text)
            print("Topics - ",data2.text)
            print("Brief Description - ",data3.text)
            print("Organisation link - ",data4.text)
            print("\n")
            driver.close()
        driver.switch_to.window(parent_window1)

#go to next page i.e 101-198 organisations
next_page = driver.find_element(By.XPATH, '//button[@aria-label="Next page"]')
driver.execute_script("arguments[0].click();", next_page)
time.sleep(5)

parent_window2 = driver.current_window_handle

##selecting and itteratiing over all organisation 101-198
organisations2 = driver.find_elements('xpath','//div[@class="info"]')

for organisation in organisations2:
    print(organisation.text)
    driver.execute_script("arguments[0].click();", organisation)

    # handling new window and itterating over current two windows
    child_windows = driver.window_handles
    for child in child_windows:
        # if new window is opened switch to new window
        if parent_window2!=child:
            driver.switch_to.window(child)
            time.sleep(5)
            data1 = driver.find_element('xpath','//div[@class="tech__content"]')
            data2 = driver.find_element('xpath','//div[@class="topics__content"]')
            data3 = driver.find_element('xpath', '//div[@class="bd"]')
            data4 = driver.find_element('xpath', '//a[@class="link"]')

            Technologies.append(data1)
            Topics.append(data2)
            Brief_Description.append(data3)
            Links.append(data4)

            print("Technologies - ",data1.text)
            print("Topics - ",data2.text)
            print("Brief Description - ", data3.text)
            print("Organisation link - ", data4.text)
            print("\n")
            driver.close()
        driver.switch_to.window(parent_window2)

File = pd.DataFrame({'Description': Brief_Description, 'TechStack': Technologies, 'Topics': Topicst, 'Link': Links})
File.to_json("JSON_FILE.txt")
driver.quit()


