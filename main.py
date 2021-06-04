##https://pypi.org/project/webdriver-manager/##

from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common import keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class GoogleKeywordSCreenshooter:
    def __init__(self,keyword,max_page,screenshots_dir):
        options = Options()
        options.add_argument("window-size=1400,600")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options = options)
        self.browser.get("https://google.com")
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
        self.max_page = max_page

    def start(self):
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        page = 1
        i = 1
        while page <= self.max_page:
            questions = self.browser.find_elements_by_class_name("rTylWd")
            people_also_ask= self.browser.find_elements_by_class_name("g-blk")
            false_elements = questions + people_also_ask
            for element in false_elements:
                self.browser.execute_script(
                """
                const false_element = arguments[0];
                false_element.parentElement.removeChild(false_element)
                """, element)
            search_results = self.browser.find_elements_by_class_name("g")
            for search_result in search_results:
                class_name = search_result.get_attribute("class")
                if class_name == "g":
                    search_result.screenshot(f"{self.screenshots_dir}/{self.keyword}_{i}.png")
                    i = i+1
            try:
                pagination = self.browser.find_element_by_class_name("AaVjTc")
                pagination.find_element_by_id("pnnext").click()
                page = page+1
            except Exception:
                break

    def finish(self):
        self.browser.quit()

vietnam_search_results = GoogleKeywordSCreenshooter("vietnam", 5,"screenshots_vietnam")
vietnam_search_results.start()
vietnam_search_results.finish()


pythonAI_serach_results = GoogleKeywordSCreenshooter("python AI", 5,"screenshots_python")
pythonAI_serach_results.start()
pythonAI_serach_results.finish()

hangxomtay_results = GoogleKeywordSCreenshooter("hang xom tay", 5,"screenshots_hangxomtay")
hangxomtay_results.start()
hangxomtay_results.finish()
