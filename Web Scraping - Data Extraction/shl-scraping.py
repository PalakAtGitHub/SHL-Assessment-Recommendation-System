from playwright.sync_api import sync_playwright
import pandas as pd
from urllib.parse import urlencode

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"
ITEMS_PER_PAGE = 12
TOTAL_ITEMS = 372  # ~32 pages × 12 items

# Example competency map
competency_map = {
    'A': 'Attention to Detail',
    'B': 'Business Communication',
    'C': 'Critical Thinking',
    'D': 'Data Interpretation',
    'E': 'Emotional Intelligence',
    'F': 'Financial Acumen',
    'G': 'Global Awareness',
    'H': 'Hiring Skills',
    'I': 'Innovation',
    'J': 'Judgment and Decision Making',
    'K': 'Knowledge of Subject',
    'L': 'Leadership',
    'M': 'Motivation',
    'N': 'Negotiation Skills',
    'O': 'Organizational Skills',
    'P': 'Problem Solving',
    'Q': 'Quality Focus',
    'R': 'Risk Management',
    'S': 'Sales Skills',
    'T': 'Teamwork',
    'U': 'Understanding Customer Needs',
    'V': 'Verbal Communication',
    'W': 'Work Ethic'
}

def extract_competencies_from_codes(codes):
    """Convert competency letter codes to full competency names"""
    codes = codes.replace(" ", "").split(",")
    return [competency_map.get(code, code) for code in codes if code]

def get_page_urls():
    """Generate all paginated URLs to scrape"""
    urls = []
    for start in range(0, TOTAL_ITEMS, ITEMS_PER_PAGE):
        params = {
            'start': start,
            'type': 1
        }
        urls.append(f"{BASE_URL}?{urlencode(params, doseq=True)}")
    return urls

def scrape_shl_page(page, url):
    """Scrape a single page of the catalog"""
    page_data = []

    print(f"Navigating to: {url}")
    page.goto(url, timeout=60000)
    page.wait_for_selector('tbody tr', timeout=10000)

    rows = page.query_selector_all('tbody tr')
    print(f"Found {len(rows)} assessments on this page")

    for row in rows:
        try:
            # Title
            title_elem = row.query_selector('td.custom__table-heading__title')
            title_text = title_elem.inner_text().strip() if title_elem else ''

            # Link
            link_elem = title_elem.query_selector('a') if title_elem else None
            link_href = link_elem.get_attribute('href') if link_elem else ''
            link = f"https://www.shl.com{link_href}" if link_href else ''

            # Competencies
            competencies_elem = row.query_selector('td.product-catalogue__keys')
            competencies_text = competencies_elem.inner_text().strip() if competencies_elem else ''

            # Map codes to names
            competencies_full = extract_competencies_from_codes(competencies_text)

            page_data.append({
                "Title": title_text,
                "Link": link,
                "Competencies": competencies_full
            })
        except Exception as e:
            print(f"Error scraping a row: {e}")
    
    return page_data

def scrape_shl_catalog():
    """Scrape the entire SHL catalog"""
    all_data = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        urls = get_page_urls()
        for url in urls:
            page_data = scrape_shl_page(page, url)
            all_data.extend(page_data)
        
        browser.close()

    return all_data

def save_to_csv(data, filename="shl_catalog.csv"):
    """Save scraped data to a CSV file"""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} assessments to {filename}")

if __name__ == "__main__":
    scraped_data = scrape_shl_catalog()
    df = pd.DataFrame(scraped_data)
    df.to_csv('shl_catalog.csv', index=False)
