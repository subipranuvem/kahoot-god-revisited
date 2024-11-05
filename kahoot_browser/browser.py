from enum import StrEnum
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class XPaths(StrEnum):
    QUESTION_XPATH: str = '//span[@role="heading"]'
    ALTERNATIVES_XPATH: str = '//*[@type="button"]//p'
    ALTERNATIVE_CLICK_XPATH: str = '//*[@type="button"]'
    CORRECT_XPATH: str = '//div[@type="Correct"]/div'
    ERROR_XPATH: str = '//div[@type="Wrong"]/div'


class KahootBrowser:
    def __init__(self) -> None:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        opts = Options()
        opts.add_argument("--width=1024")
        opts.add_argument("--height=1024")
        opts.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        )
        self._driver: webdriver.Remote = driver

    def close(self) -> None:
        try:
            self._driver.close()
        except:
            pass

    def go_to_quiz(self, quiz_url: str) -> None:
        self._driver.get(quiz_url)

    def get_question_and_alternatives(self) -> str:
        question_element = self._driver.find_element(By.XPATH, XPaths.QUESTION_XPATH)
        alternative_elements = self._driver.find_elements(
            By.XPATH, XPaths.ALTERNATIVES_XPATH
        )
        text = question_element.text
        alternative_number = 1
        for alternative_element in alternative_elements:
            text += f"\n{alternative_number} - {alternative_element.text.strip(".")}"
            alternative_number += 1
        return text

    def click_correct_alternative(self, correct_alternative: int) -> None:
        xpath = f"{XPaths.ALTERNATIVE_CLICK_XPATH}[{correct_alternative}]"
        button = self._driver.find_element(By.XPATH, xpath)
        button.click()
