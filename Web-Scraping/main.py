from scraper.category_scraper import scrape_category

if __name__ == '__main__':
    categories = {
        'Laptops': 'https://www.pacifiko.com/laptops',
        'Monitores': 'https://www.pacifiko.com/monitores',
        'Tablets': 'https://www.pacifiko.com/tablets'
    }

    for category_name, url in categories.items():
        scrape_category(url, category_name)
