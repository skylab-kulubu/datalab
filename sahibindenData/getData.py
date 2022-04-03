
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


#For windows run below
'''
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
'''

#For mac run below
driver = webdriver.Chrome(ChromeDriverManager().install())


THING = "Otomobil"


def go_website(THING,driver):
    driver.get("https://www.sahibinden.com")

    try:
        time.sleep(1)
        thing = driver.find_element_by_xpath("//*[@id='container']/div[3]/div/aside/div[1]/nav/ul[4]/li[2]/ul/li[1]/a")
        thing.click()
        try:
            all_the_things_she_said = driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[1]/div[1]/div[1]/a")
            all_the_things_she_said.click()
            time.sleep(0.5)
            
            try:
                driver.refresh()
                thats_what_she_said = driver.find_element_by_xpath("//*[@id='searchResultsSearchForm']/div/div[3]/div[4]/div[2]/ul/li[2]/a")
                driver.execute_script('arguments[0].click()', thats_what_she_said)
            
            except:
                print("[INFO]:That's what she said")
        except:
            print("[INFO]:Didnt find the kiddo2")
    except:
        print("[INFO]: Didnt find the kiddo")    

def go_inside():
    pass

def collect_rewards():
    pass


def come_back():
    pass


def get_data(driver):
    driver.get("https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&pagingSize=50&category=3530")
    driver.refresh()

    kill_me = driver.find_elements_by_class_name("searchResultsGalleryContent")
    print(kill_me)

    
#go_website(THING,driver)
get_data(driver=driver)
