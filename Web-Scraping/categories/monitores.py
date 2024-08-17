from scraper.category_scraper import scrape_category

def scrape_monitores():
    url = 'https://www.pacifiko.com/monitores'
    scrape_category(url, 'Monitores')
