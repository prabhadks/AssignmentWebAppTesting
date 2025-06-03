from pages.base_page import BasePage
from utils.logger import get_logger

from selenium.webdriver.common.by import By
from components.footer_component import FooterComponent

class HomePage(BasePage):
    ACCEPT_BTN = (By.XPATH, "//div[text() = 'Accept']")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)
        self.footer = FooterComponent(driver, self.common_element_actions)

    def is_page_ready(self):
        self.logger.info("Navigating to home page and waiting to accept the cookies banner...")
        return self.common_element_actions.click_element(self.ACCEPT_BTN)