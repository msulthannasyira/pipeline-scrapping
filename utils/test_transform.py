import pytest
from bs4 import BeautifulSoup
from utils.transform import parse_product

sample_html = """
<div class="product-details">
  <h3>Test Jacket</h3>
  <p class="price">$25.00</p>
  <p>Rating: 4.5/5 ⭐</p>
  <p>Colors: 3</p>
  <p>Size: M</p>
  <p>Gender: Unisex</p>
</div>
"""

def test_parse_product_valid():
    soup = BeautifulSoup(sample_html, 'html.parser')
    product = soup.select_one('div.product-details')
    parsed = parse_product(product)

    assert parsed is not None
    assert parsed['Title'] == "Test Jacket"
    assert parsed['Price'] == 400000
    assert parsed['Rating'] == 4.5
    assert parsed['Colors'] == 3
    assert parsed['Size'] == "M"
    assert parsed['Gender'] == "Unisex"
    assert 'Timestamp' in parsed

def test_parse_product_invalid():
    bad_html = """<div class="product-details"><h3>Unknown Product</h3></div>"""
    soup = BeautifulSoup(bad_html, 'html.parser')
    product = soup.select_one('div.product-details')
    parsed = parse_product(product)

    assert parsed is None
