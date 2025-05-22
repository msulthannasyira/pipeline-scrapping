import time
from utils.extract import fetch_page
from utils.transform import parse_products_from_soup
from utils.load import save_to_csv

BASE_URL = "https://fashion-studio.dicoding.dev"

def main():
    all_products = []

    print("Scraping page 1...")
    soup = fetch_page(BASE_URL)
    if soup:
        all_products += parse_products_from_soup(soup)

    for page_num in range(2, 51):
        print(f"Scraping page {page_num}...")
        page_url = f"{BASE_URL}/page{page_num}"
        soup = fetch_page(page_url)
        if not soup:
            print(f"No products found on page {page_num}, stop scraping.")
            break
        products = parse_products_from_soup(soup)
        if not products:
            break
        all_products += products
        time.sleep(1)

    save_to_csv(all_products)

if __name__ == "__main__":
    main()
