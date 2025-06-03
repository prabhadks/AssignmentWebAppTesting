from selenium.webdriver.common.by import By

from utils.logger import get_logger

logger = get_logger(__name__)
class FooterComponent:
    browse_locator = (By.XPATH, "//div[text()='Browse']/../parent::a[@href='/directory']")

    def __init__(self, driver, common_element_actions):
        self.driver = driver
        self.common_element_actions = common_element_actions


    def click_browse(self):
        logger.info("Clicking on Browser icon...")
        return self.common_element_actions.click_element(self.browse_locator)