# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from faker import Faker
from selenium.common.exceptions import WebDriverException


# constants
# invite_url = 'https://xrpspin.com/5155435669361967?' real one

# proxies from http://free-proxy.cz/en/
with open('http.txt') as nyau:
    proxy_list = nyau.readlines()

invite_url = 'https://xrpspin.com/4748220927330365?'
password = 'matako'

for proxy in proxy_list:
    print(proxy)
    try:
        fake_name = Faker().name()
        email = f"{fake_name.replace(' ','')}{random.randint(1,999)}@gmail.com"

        options = Options()
        options.add_argument('--proxy-server={}'.format(proxy))
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options)
        driver.maximize_window()

        # start the browser
        driver.get(invite_url)
        driver.find_element(By.XPATH, '//a[@href="register.php"]').click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'register')))
        # fill the form
        driver.find_element(By.ID, 'username').send_keys(fake_name.lower())
        driver.find_element(By.ID, 'fullname').send_keys(fake_name)
        driver.find_element(By.ID, 'email').send_keys(email.lower())
        driver.find_element(By.ID, 'phone').send_keys(random.randrange(435728191, 473829273))
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'repassword').send_keys(password)
        sleep(3)
        driver.find_element(By.ID, 'register').click()
        sleep(8)
    except WebDriverException as e:
        print(e.msg)
        sleep(1)
    driver.quit()