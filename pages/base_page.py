from abc import ABC, abstractmethod
from utils.logger import get_logger
from utils.common_element_actions import ElementActions

logger = get_logger(__name__)

class BasePage(ABC):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.common_element_actions = ElementActions(driver, timeout)

    @abstractmethod
    def is_page_ready(self):
        """
        Abstract method for page readiness check.
        """
        pass