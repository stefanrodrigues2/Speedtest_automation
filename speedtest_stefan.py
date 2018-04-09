import os
import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
os.path.join(os.path.dirname(__file__), p)
)

def runSpeedTestAppAutomation():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'fcb7c8320104',
        'app': PATH('C:/Users/VIO PC/Desktop/speedtest_ookla.apk'),
        'newCommandTimeout': 240
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
   
    time.sleep(5)
    element = driver.find_element_by_class_name('android.view.View')
    action = TouchAction(driver)
    action.tap(element).perform()
    start = time.time()  
    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.ID, "org.zwanoo.android.speedtest:id/shareIcon")))
    final = time.time()
    print "Time taken is {}\n".format(final-start)
    
    time.sleep(5)
    driver.quit()
    return
	
	


if __name__ == "__main__":
    runSpeedTestAppAutomation()

