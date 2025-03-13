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
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Test Explanations

### 1. test_add_product
**Purpose:** Ensure that adding a product to the inventory works correctly.

**How it Works:**
- A sample product (e.g., "MacBook") is added to the inventory.
- The test retrieves the product by its name.
- It asserts that the product exists and that its attributes (name, price, quantity) match the expected values.

### 2. test_remove_product
**Purpose:** Verify that removing a product from the inventory is handled properly.

**How it Works:**
- A product is added to the inventory.
- The product is then removed by its name.
- The test confirms that the product no longer exists in the inventory (retrieving it returns `None`).

### 3. test_total_inventory_value
**Purpose:** Confirm that the total inventory value is computed correctly.

**How it Works:**
- Multiple products are added to the inventory.
- The test calculates the total value (price multiplied by quantity for each product).
- It verifies that the computed total matches the expected sum.

### 4. test_get_nonexistent_product
**Purpose:** Check the behavior when retrieving a product that does not exist.

**How it Works:**
- The test attempts to retrieve a product using a name that isn’t present in the inventory.
- It asserts that the function returns `None`, which is the expected behavior.

## Running Tests with pytest:
  **Run all tests:**
  ```bash
  pytest -v tests/test_inventory.py::TestInventory
  ```
  **Run a specific test:**
  ```bash
  pytest -v tests/test_inventory.py -k test_add_product
  ```
