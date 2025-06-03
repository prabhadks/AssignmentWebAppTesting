import random
from utils.logger import get_logger

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.footer_component import FooterComponent

class DirectoryPage(BasePage):
    SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
    STREAMER_LOCATOR = (By.XPATH, "//img[@class='tw-image']")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)
        self.footer = FooterComponent(driver, self.common_element_actions)

    def is_page_ready(self):
        self.logger.info("Waiting for Search Element to appear...")
        self.common_element_actions.wait_for_element(self.SEARCH_FIELD)

    def enter_text_to_search(self, search_term):
        self.logger.info(f"Entering {search_term} into Search field...")
        search_element = self.common_element_actions.wait_for_element(self.SEARCH_FIELD)
        self.common_element_actions.send_keys(self.SEARCH_FIELD, search_term)
        search_element.send_keys(Keys.ENTER)

    def scroll(self):
        self.logger.info("Scroll page down once")
        self.common_element_actions.scroll_page_down()

    def wait_for_images_to_load(self):
        self.logger.info("Waiting for the images to load...")
        self.common_element_actions.wait_for_all_images_to_load(20)

    def get_all_streamers(self):
        self.logger.info("Get all the video streamers...")
        return self.common_element_actions.wait_for_elements(self.STREAMER_LOCATOR)

    def select_and_click_random_streamer(self):
        self.logger.info("Select randomly a streamer and click")
        streamers_list = self.get_all_streamers()
        streamer = random.choice(streamers_list)
        streamer_index = streamers_list.index(streamer)

        streamer_refresh = self.common_element_actions.wait_for_element(self.STREAMER_LOCATOR, timeout=20, index=streamer_index)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", streamer_refresh)
        self.common_element_actions.scroll_into_view(streamer_refresh)
        self.common_element_actions.click_element(self.STREAMER_LOCATOR, index=streamer_index)