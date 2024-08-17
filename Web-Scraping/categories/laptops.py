from scraper.category_scraper import scrape_category

def scrape_laptops():
    url = 'https://www.pacifiko.com/laptops'
    scrape_category(url, 'Laptops')
