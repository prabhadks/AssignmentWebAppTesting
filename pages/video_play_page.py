from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.logger import get_logger

class VideoPlayPage(BasePage):
    VIDEO_LOCATOR = (By.TAG_NAME, "video")
    START_WATCHING_BTN = (By.XPATH, "//div[text()='Start Watching']/../parent::button")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def is_page_ready(self):
        self.logger.info("On Video playing page...")

    def get_video_element(self):
        return self.common_element_actions.wait_for_element(self.VIDEO_LOCATOR)

    def play_video(self):
        video_ready = self.common_element_actions.wait_for_video_to_completely_load(self.get_video_element(), 10)

        if not video_ready:
            self.logger.info("Video is not ready. Trying to play manually...")
            start_watching_btn = self.common_element_actions.wait_for_element(self.START_WATCHING_BTN, 10)
            self.common_element_actions.click_enabled_element(start_watching_btn)
            assert self.common_element_actions.wait_for_video_to_completely_load(self.get_video_element(),
                                                                                             10), f"Video not completely loaded"

    def take_screenshot_video(self, file_name):
        self.common_element_actions.take_screenshot(file_name)