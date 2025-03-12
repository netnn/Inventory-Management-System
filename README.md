# Inventory Management System

A simple Python inventory management system demonstrating object-oriented design, automated testing with `pytest`, and Git version control.

## Repository

This project is hosted on GitHub: [Inventory Management System](https://github.com/netnn/Inventory-Management-System)

## Project Structure

- **inventory/**: Contains the source code:
  - `product.py` – Defines the `Product` class.
  - `inventory.py` – Implements the `Inventory` class with methods to add, remove, and retrieve products, and to calculate total inventory value.
- **tests/**: Contains test files:
  - `test_inventory.py` – Unit tests for the inventory system.
  - `conftest.py` – Fixtures used by the tests.
- **requirements.txt**: Lists the project dependencies (e.g., `pytest`).
- **README.md**: This file.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/netnn/Inventory-Management-System.git
   cd Inventory-Management-System
   ```
2. **(Optional) Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```
   - On Windows (CMD):
     ```bash
     venv\Scripts\activate
     ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests with pytest:
  **Run all tests:**
  ```bash
  pytest -v tests/test_inventory.py::TestInventory
  ```
  **Run a specific test:**
  ```bash
  pytest -v tests/test_inventory.py -k test_add_product
  ```

## Using the Inventory System
  **Here is a simple example of how to use the system in your Python code:**
  ```bash
  from inventory.inventory import Inventory
  from inventory.product import Product

  # Create an inventory and add a product
  inv = Inventory()
  inv.add_product(Product("Laptop", 1000, 5))
  
  # Print the total inventory value
  print(f"Total inventory value: {inv.total_inventory_value()}")
  ```


