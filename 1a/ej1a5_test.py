import pytest
from ej1a5 import add_product, find_product, list_products, inventory, Product

@pytest.fixture
def setup_inventory():
    inventory.clear()


def test_add_product(setup_inventory):
    product = add_product("Bananas", "Fruits", 30, 0.45)
    assert product.name == "Bananas", "The product name should be 'Bananas'."
    assert product.category == "Fruits", "The product category should be 'Fruits'."
    assert product.quantity == 30, "The quantity of 'Bananas' should be 30."
    assert product.price == 0.45, "The price of 'Bananas' should be 0.45."

def test_find_product(setup_inventory):
    add_product("Mangoes", "Fruits", 15, 1.00)
    product = find_product("Mangoes", "Fruits")
    assert product is not None, "The product 'Mangoes' should be found."
    assert product.name == "Mangoes", "The product name should be 'Mangoes'."
    assert product.quantity == 15, "The quantity of 'Mangoes' should be 15."
    assert product.price == 1.00, "The price of 'Mangoes' should be 1.00."

def test_find_nonexistent_product(setup_inventory):
    """Test attempting to find a product that doesn't exist."""
    product = find_product("Nonexistent", "Product")
    assert product is None, "A nonexistent product should not be found."

def test_list_products(setup_inventory):
    add_product("Bananas", "Fruits", 30, 0.45)
    expected_output = "Bananas (Fruits) - 30 units at $0.45 each"
    assert list_products() == expected_output, "The list_products output should match the expected output."
