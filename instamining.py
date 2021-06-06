import time
from selenium import webdriver
from typing import KeysView
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


INSTAGRAM_ID = "id"
INSTAGRAM_PASSWORD = "password"
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.instagram.com/accounts/login/")
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ")))



insta_id = browser.find_element_by_name("username")
insta_password = browser.find_element_by_name("password")

insta_id.send_keys(INSTAGRAM_ID)
insta_password.send_keys(INSTAGRAM_PASSWORD)

insta_password.send_keys(Keys.ENTER)

main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")

header = browser.find_element_by_tag_name("header")
hashtags = header.find_elements_by_class_name("AC7dP")
print(hashtags)