from playwright.sync_api import Playwright, sync_playwright, expect

# python -m playwright codegen

import re
from playwright.sync_api import Playwright, sync_playwright, expect
from selenium.webdriver.common.devtools.v136.debugger import pause


def run(playwright: Playwright) -> None:
    # access - given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # open new page
    page = context.new_page()
    # Open website - https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    # Act - When/And
    # Click button: has-text("Log in")

    # page.wait_for_selector('#handle-button')
    # page.get_by_test_id("handle-button").wait_for()
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("example@lol.pt")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("asdfrw")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # assert page.is_visible("text=Celebrating Beauty and Style")
    expect(page.locator("text=Celebrating Beauty and Style")).to_be_visible()
    page.pause()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
