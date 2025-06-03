import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from pages.directory_page import DirectoryPage
from pages.home_page import HomePage
from pages.video_play_page import VideoPlayPage

load_dotenv(dotenv_path="application_config.env")

@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("mobileEmulation", {"deviceName": os.getenv("DEVICE_NAME")})
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def directory_page(driver):
    return DirectoryPage(driver)

@pytest.fixture
def video_play_page(driver):
    return VideoPlayPage(driver)