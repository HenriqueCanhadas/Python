from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        color_scheme='dark',
        record_video_dir='.'
    )

    page = context.new_page()
    page.goto("https://playwright.dev/")
    sleep(5)
    print(page.title())
    browser.close()
