from inventory.product import Product

class TestInventory:
    def test_add_product(self, inventory, return_sample_product):
        inventory.add_product(return_sample_product)
        retrieved = inventory.get_product("MacBook")
        assert retrieved is not None
        assert retrieved.name == "MacBook"
        assert retrieved.price == 4000.0
        assert retrieved.quantity == 7

    def test_remove_product(self, inventory, return_sample_product):
        inventory.add_product(return_sample_product)
        inventory.remove_product("MacBook")
        assert inventory.get_product("MacBook") is None

    def test_total_inventory_value(self, inventory):
        # Add a few products
        p1 = Product(name="MagicMouse", price=250.0, quantity=2)
        p2 = Product(name="MagicKeyboard", price=350.0, quantity=1)
        inventory.add_product(p1)
        inventory.add_product(p2)
        assert inventory.total_inventory_value() == 850.0

    def test_get_nonexistent_product(self, inventory):
        # Case when the product does not exist
        product = inventory.get_product("MacBookAir")
        assert product is None
