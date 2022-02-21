# fmt: off
import collections
import unidecode
import time
import sys
import shutil
import re
import pdb
import os.path
import os
from cprint import *
import logging
import locale
import json
import chromedriver_autoinstaller
import art 
import argparse
import pwinput
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from os.path import abspath
from inspect import getmembers
from datetime import datetime, timedelta


def configure_firefox_driver_profile(dn, profile_folder_path):
    options = Options()
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.update_preferences()
    desired = DesiredCapabilities.FIREFOX
    service = Service(os.path.join(dn, "geckodriver-v0.30.0-win64.exe"))
    firefox = webdriver.Firefox(desired_capabilities=desired, service=service)
    return firefox


def configure_firefox_driver_no_profile(dn):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--private')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('referer=https://www.google.com/')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument('--disable-blink-featuresi=AutomationControlled')
    options.add_argument('--disable-blink-features')
    options.set_preference('excludeSwitches', 'enable-automation')
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.set_preference("browser.privatebrowsing.autostart", True)
    service = Service(os.path.join(dn, "geckodriver-v0.30.0-win64.exe"))
    firefox = webdriver.Firefox(options=options, service=service)
    firefox.get('about:home')
    firefox.maximize_window()
    return firefox


def configure_chrome_driver_no_profile(dn):
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("disable-infobars")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome = webdriver.Chrome(options=options, executable_path="ChromeDriver 98.0.4758.80.exe")
    return chrome

def configure_chrome_driver_default_profile(dn):
    # chrome://version/ get profile path
    # C:\Users\osvaldohm\AppData\Local\Temp\scoped_dir6512_509824382\Default
    profile_path = r"C:\Users\osvaldohm\AppData\Local\Temp\scoped_dir6512_509824382\Default"
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("disable-infobars")
    options.add_argument("user-data-dir={}".format(profile_path)) #Path to your chrome profile
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome = webdriver.Chrome(options=options, executable_path="ChromeDriver 98.0.4758.80.exe")
    return chrome


# User interpreter.
#def main():
dn = os.getcwd()
print("Opening selenium...")
chrome = configure_chrome_driver_default_profile(dn)
chrome.get("https://es.scribd.com/")

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consequat finibus molestie. Mauris nibh metus, suscipit quis rutrum eget, posuere vitae enim. Sed vitae leo risus. Etiam efficitur elementum arcu, sit amet porttitor nibh mollis quis. Phasellus tempus nulla vitae arcu fringilla pellentesque. Vivamus eu sapien laoreet, faucibus odio in, ullamcorper magna. Integer nibh massa, pretium eget tincidunt vitae, elementum vitae dolor. Vestibulum in mollis nibh. Nullam varius tellus nisi, non convallis erat posuere nec. In hac habitasse platea dictumst."

elements =  chrome.find_elements(By.CLASS_NAME , 'description_input')
for description_area in element:
    description_area.send_keys()

print(len(elements))

a = driver.find_elements_by_class_name("content")


if __name__ == "__main__":
    main()
