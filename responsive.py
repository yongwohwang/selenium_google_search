import time
from math import ceil, floor
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class ResponsiveTester:
    def __init__(self,urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [480,960,1366,1920]
    def sitename(self,url):
        site_name = url
        site_name = site_name.split("https://")[1].split('/')[0]
        site_name = site_name.replace(".","_")
        print(site_name)
        return site_name
    def screenshot(self, url):
        self.browser.get(url)
        site_name = self.sitename(url)
        for size in self.sizes:
            current_screen= self.browser.get_window_size()
            self.browser.set_window_size(size,current_screen['height'])
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            browser_h = self.browser.execute_script("return window.innerHeight")
            section_size = 0
            i = 1
            time.sleep(1)
            while section_size < scroll_size:
                self.browser.execute_script(f"window.scrollTo(0,{section_size})")
                self.browser.save_screenshot(f"screenshots/{site_name}_{size}_{i}.png")
                time.sleep(1)
                section_size = section_size + browser_h
                i = i + 1
            self.browser.execute_script("window.scrollTo(0,0)")

    
    def start(self):
        for url in self.urls:
            self.screenshot(url)
    def finish(self):
        self.browser.quit()


tester = ResponsiveTester(["https://www.facebook.com/", "https://nomadcoders.co/", "https://www.naver.com"])
tester.start()
tester.finish()