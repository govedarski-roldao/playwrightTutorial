from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Rodolfo", "Sofia", "test@email.com", "123-234-25874", "test subject", "test message")

# with sync_playwright() as playwright:
#     test_submit_form(playwright)
#     time.sleep(5)
