import getpass
from re import sub

import keyring
import selenium
import pickle

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


def load_driver(chromedriver_path="E:\PythonEnv\IBTrading\driver\chromedriver.exe"):
    driver = Chrome(executable_path=chromedriver_path)
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def get_credentials(service_name):
    credentials = keyring.get_credential(service_name, None)
    if credentials is None:
        username = input("Username: ")
        password = getpass.getpass()
        keyring.set_password(service_name,username, password)
    else:
        username = credentials.username
        password = credentials.password
    return username,password

def save_cookie(driver, path='./data/cookie.pkl'):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path='./data/cookie.pkl'):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)