from scraper.category_scraper import scrape_category

def scrape_tablets():
    url = 'https://www.pacifiko.com/tablets'
    scrape_category(url, 'Tablets')
