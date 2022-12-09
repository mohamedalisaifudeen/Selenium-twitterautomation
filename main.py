from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver import Edge, Keys
from selenium.webdriver.edge.service import Service
from speedcheck import Speed
import time

import os

s_p=Speed()
s_p.airtel()

driver=Service(executable_path=EdgeChromiumDriverManager().install())
new_driver=Edge(service=driver)
# os.environ.get(key='twitter')
new_driver.get(url="https://twitter.com/i/flow/login")

new_driver.implicitly_wait(20)

user_name=new_driver.find_element(by=By.NAME,value='text')
new_driver.implicitly_wait(4)
user_name.send_keys("alirox130@gmail.com")
user_name.send_keys(Keys.ENTER)
new_driver.implicitly_wait(20)

password=new_driver.find_element(By.NAME,value='password')
new_driver.implicitly_wait(20)
password.send_keys(os.environ.get('twitter'))
new_driver.implicitly_wait(10)
password.send_keys(Keys.ENTER)

time.sleep(8)
tweet=new_driver.find_element(by=By.CLASS_NAME,value='css-901oao7')
tweet.send_keys(f"The download speed is {s_p.download} and the upload speed is {s_p.upload} not as promised @AirtelSrilanka \n #AirtelSrilanka")
tweet.send_keys(Keys.ENTER)



new_driver.implicitly_wait(60)
new_driver.quit()


