class Product:
    """
    Class representing a single product in the system.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param price: The unit price of the product (must be non-negative).
        :param quantity: The quantity of the product in stock (must be non-negative).
        """
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self) -> float:
        """
        Returns the total value of the product (price * quantity).
        """
        return self.price * self.quantity

    def __repr__(self):
        return f"\n\nProduct(name={self.name}, price={self.price}, quantity={self.quantity})"
