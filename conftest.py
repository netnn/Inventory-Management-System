import pytest
from inventory.inventory import Inventory
from inventory.product import Product

@pytest.fixture
def inventory():
    """
    Fixture that returns a new Inventory object before each test.
    """
    return Inventory()

@pytest.fixture
def return_sample_product():
    """
    Fixture that returns a sample product for testing.
    """
    return Product(name="MacBook", price=4000.0, quantity=7)
