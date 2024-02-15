from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any
import logging
import sys

logging.basicConfig(
    format='[%(asctime)s][%(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
    handlers=[logging.FileHandler("RPA.log"), logging.StreamHandler(sys.stdout)]
)

class WebElement:
    def __init__(self, element=None) -> None:
        self.element = element
    
    def __call__(self) -> Any:
        return self.element
    
    def inner_text(self) -> str | None:
        return self.element.get_attribute('innerText')
    
    def get_attribute(self, attr: str) -> str | None:
        return self.element.get_attribute(attr)
    
    def query_selector_all(self, selector) -> list:
        return [WebElement(el) for el in self.element.find_elements(By.CSS_SELECTOR, selector)]
    
    def query_selector(self, selector):
        return WebElement(self.element.find_element(By.CSS_SELECTOR, selector))

    def click(self) -> None:
        self.element.click()

    def get_element(self) -> Any:
        return self.element

class Browser:
    DEFAULT_TIMEOUT = 10

    def __init__(self, *args) -> None:
        options = webdriver.ChromeOptions()
        for arg in args:
            options.add_argument(arg)
        self.browser = webdriver.Chrome(options=options)

    def navigate_to(self, url:str) -> None:
        logging.info("Launching browser")
        self.browser.get(url)
    
    def wait_for_navigation(self, timeout:int=DEFAULT_TIMEOUT) -> bool:
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(lambda x: self.browser.execute_script("return document.readyState")=="complete")
    
    def wait_for_element_located(self, selector:str, type_:str=By.CSS_SELECTOR, timeout:int=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.presence_of_element_located((type_, selector)))
    
    def wait_for_element_visible(self, selector:str, type_:str=By.CSS_SELECTOR, timeout:int=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.browser, timeout)
        return wait.until(EC.visibility_of_element_located((type_, selector)))

    def query_selector(self, selector:str):
        return self.browser.find_element(By.CSS_SELECTOR, selector)
    
    def query_selector_all(self, selector:str):
        return [WebElement(el) for el in self.browser.find_elements(By.CSS_SELECTOR, selector)]

    def close(self):
        logging.info("Closing browser")
        self.browser.quit()