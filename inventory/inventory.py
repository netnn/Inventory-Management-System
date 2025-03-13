from .product import Product

class Inventory:
    """
    Class for managing product inventory.
    Stores a list of Product objects and provides basic operations.
    """

    def __init__(self):
        # Products can be stored in a list or a dictionary. Here we choose a list.
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the inventory.
        """
        self.products.append(product)

    def remove_product(self, product_name: str, raise_error: bool = False):
        """
        Remove a product from the inventory by product name.
        If the product is not found, do nothing or optionally raise an error.

        :param product_name: The name of the product to remove.
        :param raise_error: If True, raise a ValueError when the product is not found.
        """
        found = any(p for p in self.products if p.name.lower() == product_name.lower())
        if not found and raise_error:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
        self.products = [
            p for p in self.products if p.name.lower() != product_name.lower()
        ]

    def get_product(self, product_name: str, raise_error: bool = False) -> None:
        """
        Retrieve a product from the inventory by product name.
        Returns None if not found, or optionally raises an error.

        :param product_name: The name of the product to retrieve.
        :param raise_error: If True, raise a ValueError when the product is not found.
        :return: The Product object or None.
        """
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        if raise_error:
            raise ValueError(f"Product '{product_name}' not found in inventory.")
        return None

    def total_inventory_value(self) -> float:
        """
        Calculate the total inventory value based on the value of each product.
        """
        return sum(p.total_value() for p in self.products)

    def __repr__(self):
        return f"\n\nInventory with {len(self.products)} products."
