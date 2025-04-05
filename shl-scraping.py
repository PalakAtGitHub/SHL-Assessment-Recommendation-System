from playwright.sync_api import sync_playwright
import csv

CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"

# Mapping of letter codes to full competency names
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

# Function to map codes to competencies
def extract_competencies_from_codes(codes):
    competencies = []
    for char in codes:
        char = char.strip().upper()
        if char in competency_map:
            competencies.append(competency_map[char])
    return competencies

# Main scraping function
def scrape_shl_catalog():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Navigating to catalog page...")
        page.goto(CATALOG_URL, timeout=60000)
        page.wait_for_timeout(5000)  # Allow some time for the page to load

        print("Scraping assessments...")
        rows = page.query_selector_all('tbody tr')

        for row in rows:
            try:
                # Extract title
                title_elem = row.query_selector('td.custom__table-heading__title')
                title_text = title_elem.inner_text().strip() if title_elem else ''

                # Extract link
                link_elem = title_elem.query_selector('a') if title_elem else None
                link_href = link_elem.get_attribute('href') if link_elem else ''
                link = f"https://www.shl.com{link_href}" if link_href else ''

                # Extract competencies (letter codes)
                competencies_elem = row.query_selector('td.product-catalogue__keys')
                competencies_text = competencies_elem.inner_text().strip() if competencies_elem else ''

                # Map letter codes to full names
                competencies_full = extract_competencies_from_codes(competencies_text)

                data.append({
                    "Title": title_text,
                    "Link": link,
                    "Competencies": competencies_full
                })

            except Exception as e:
                print(f"Error processing a row: {e}")

        browser.close()

    return data

# Function to save data to CSV
def save_to_csv(data, filename='shl_catalog.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Title', 'Link', 'Competencies'])
        writer.writeheader()
        for item in data:
            writer.writerow({
                "Title": item['Title'],
                "Link": item['Link'],
                "Competencies": item['Competencies']
            })
    print(f"Data saved to {filename}")

# Entry point
if __name__ == "__main__":
    scraped_data = scrape_shl_catalog()
    save_to_csv(scraped_data)
