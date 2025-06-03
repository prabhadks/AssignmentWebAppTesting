from pytest_bdd import scenarios, given, when, then, parsers
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="application_config.env")

scenarios("../features")


@given("User go to Twitch")
def open_twitch(driver):
    driver.get(os.getenv("BASE_URL"))


@then("Twitch home page is displayed")
def navigate_home_page(home_page):
    home_page.is_page_ready()


@then("User clicks on the Search icon from home page")
def user_clicks_search(home_page):
    home_page.footer.click_browse()


@when(parsers.parse('Enters "{search_term}" in Search box'))
def user_enters_search_term(directory_page, search_term):
    directory_page.is_page_ready()
    directory_page.enter_text_to_search(search_term)
    directory_page.wait_for_images_to_load()


@when(parsers.parse("User scrolls down {count:d} times on directory page"))
def user_scrolls(directory_page, count):
    for _ in range(count):
        directory_page.scroll()


@when("User selects a streamer")
def user_selects_streamer(directory_page):
    directory_page.select_and_click_random_streamer()


@then("User is navigated to the Streamer page")
def streamer_page_displayed(video_play_page):
    video_play_page.is_page_ready()


@then("User waits till the streamer is loaded")
def play_video(video_play_page):
    video_play_page.play_video()
    video_play_page.take_screenshot_video(os.getenv("FILE_NAME"))
