from playwright.sync_api import expect, Playwright, sync_playwright
from pom.home_page_elements import HomePage


def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)

    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()

    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("example@lol.pt")
    page.get_by_role("textbox", name="Password").fill("asdfrw")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    # ✅ CORRETO: usar diretamente os locators da classe
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


# with sync_playwright() as playwright:
#     test_about_us_section_verbiage(playwright)