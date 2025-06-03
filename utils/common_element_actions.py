import os

from utils.logger import get_logger

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ElementActions:
    def __init__(self, driver, default_timeout=5):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)
        self.timeout = default_timeout

    def wait_for_element(self, by_locator, timeout=None, index=None):
        locator = self.indexed_locator(by_locator, index)
        element = self.wait(self.get_timeout(timeout)).until(
            EC.presence_of_element_located(locator)
        )
        assert element is not None, f"Element not found with locator: {locator}"
        return element

    def wait_for_elements(self, by_locator, timeout=None):
        elements = self.wait(self.get_timeout(timeout)).until(
            EC.presence_of_all_elements_located(by_locator))
        assert elements, f"No elements found for {by_locator}"
        return elements

    def wait_for_clickable(self, by_locator, timeout=None, index=None):
        locator = self.indexed_locator(by_locator, index)
        element = self.wait(self.get_timeout(timeout)).until(
            EC.element_to_be_clickable(locator)
        )
        assert element is not None, f"Element not clickable with locator: {locator}"
        return element

    def click_element(self, by_locator, timeout=None, index=None):
        self.wait_for_clickable(by_locator, self.get_timeout(timeout), index).click()

    def click_enabled_element(self, element):
        assert element.is_enabled(), f"Element not clickable with locator: {element}"
        element.click()

    def send_keys(self, by_locator, text, timeout=None):
        element = self.is_element_displayed(by_locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, by_locator, timeout=None):
        element = self.wait_for_element(by_locator, self.get_timeout(timeout))
        assert element.is_displayed(), f"Element not displayed with locator: {by_locator}"
        return element

    def get_text(self, by_locator, timeout=None):
        element = self.is_element_displayed(by_locator, timeout)
        return element.text

    def scroll_page_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    def indexed_locator(self, by_locator, index=None):
        if index is not None:
            by = by_locator[0]
            locator = f"({by_locator[1]})[{index}]"
            return by, locator
        return by_locator

    def wait(self, timeout):
        return WebDriverWait(self.driver, timeout)

    def wait_for_video_to_completely_load(self, by_locator, timeout=None):
        return self.wait(self.get_timeout(timeout)).until(
            lambda d: d.execute_script("return arguments[0].readyState === 4;", by_locator))

    def wait_for_all_images_to_load(self, timeout=None):
        self.wait(self.get_timeout(timeout)).until(
            lambda d: d.execute_script("""
                        return Array.from(document.images).every(img => img.complete && img.naturalHeight > 0)
                    """)
        )

    def get_timeout(self, timeout):
        return timeout if timeout is not None else self.timeout

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def take_screenshot(self, file_name):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)  # create folder if not exists
        filepath = os.path.join(folder, file_name)
        self.driver.save_screenshot(filepath)