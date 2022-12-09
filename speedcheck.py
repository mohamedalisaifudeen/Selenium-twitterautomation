from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver import Edge, Keys
from selenium.webdriver.edge.service import Service
import time


class Speed:
    def __init__(self):
        self.download=0
        self.upload=0

    def airtel(self):
        driver = Service(executable_path=EdgeChromiumDriverManager().install())
        new_driver = Edge(service=driver)
        # os.environ.get(key='twitter')
        new_driver.get(url="https://www.speedtest.net/")
        go = new_driver.find_element(by=By.LINK_TEXT, value='GO')
        go.click()
        time.sleep(130)
        download = new_driver.find_element(by=By.CLASS_NAME, value='download-speed').text
        upload = new_driver.find_element(by=By.CLASS_NAME, value='upload-speed').text
        self.download=download
        self.upload=upload
        new_driver.quit()







