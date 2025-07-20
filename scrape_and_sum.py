# scrape_and_sum.py
from playwright.sync_api import sync_playwright

urls = [
    "https://exam-portal.iitm.ac.in/qa/seed/60",
    "https://exam-portal.iitm.ac.in/qa/seed/61",
    "https://exam-portal.iitm.ac.in/qa/seed/62",
    "https://exam-portal.iitm.ac.in/qa/seed/63",
    "https://exam-portal.iitm.ac.in/qa/seed/64",
    "https://exam-portal.iitm.ac.in/qa/seed/65",
    "https://exam-portal.iitm.ac.in/qa/seed/66",
    "https://exam-portal.iitm.ac.in/qa/seed/67",
    "https://exam-portal.iitm.ac.in/qa/seed/68",
    "https://exam-portal.iitm.ac.in/qa/seed/69",
]

def extract_numbers_from_page(page):
    numbers = []
    tables = page.query_selector_all("table")
    for table in tables:
        rows = table.query_selector_all("tr")
        for row in rows:
            cells = row.query_selector_all("td")
            for cell in cells:
                try:
                    num = float(cell.inner_text().replace(",", "").strip())
                    numbers.append(num)
                except:
                    pass
    return numbers

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    total = 0

    for url in urls:
        page.goto(url)
        numbers = extract_numbers_from_page(page)
        total += sum(numbers)

    print(f"TOTAL SUM: {total}")
    browser.close()
