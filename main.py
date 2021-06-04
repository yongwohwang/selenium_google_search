##https://pypi.org/project/webdriver-manager/##

from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
KEYWORD = "VIETNAM"
MAX_PAGE = 10

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)
page = 1
i = 1
while page <= MAX_PAGE:
    questions = browser.find_elements_by_class_name("rTylWd")
    people_also_ask= browser.find_elements_by_class_name("g-blk")
    false_elements = questions + people_also_ask

    for element in false_elements:
        browser.execute_script(
        """
        const false_element = arguments[0];
        false_element.parentElement.removeChild(false_element)
        """, element)
    search_results = browser.find_elements_by_class_name("g")
    
    for index, search_result in enumerate(search_results):
        class_name = search_result.get_attribute("class")
        if class_name == "g":
            search_result.screenshot(f"screenshots/{KEYWORD}_{i}.png")
            i = i+1

    pagination = browser.find_element_by_class_name("AaVjTc")
    page_links = pagination.find_element_by_id("pnnext").click()
    #link = page_links.get_attribute("href")
    page = page+1
browser.quit()