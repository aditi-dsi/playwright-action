from playwright.sync_api import sync_playwright
import re

BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed="

def extract_numbers_from_text(text):
    return [float(num.replace(",", "")) for num in re.findall(r'[\d,]+\.\d+|[\d,]+', text)]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    total_sum = 0

    for seed in range(60, 70):
        url = f"{BASE_URL}{seed}"
        page.goto(url)
        page.wait_for_selector("table")

        tables = page.query_selector_all("table")
        for table in tables:
            content = table.inner_text()
            numbers = extract_numbers_from_text(content)
            total_sum += sum(numbers)

    print(f"TOTAL SUM ACROSS SEEDS 60–69: {total_sum}")
    browser.close()
