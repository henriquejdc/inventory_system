import unittest
from inventory_system.models import Product
from inventory_system.inventory import Inventory
from inventory_system.exceptions import ProductAlreadyExistsError, ProductNotFoundError

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.product = Product(1, "Teclado", 150.0, 10)

    def test_add_product(self):
        self.inventory.add_product(self.product)
        self.assertEqual(self.inventory.get_product(1).name, "Teclado")

    def test_get_non_existent_product_raises(self):
        with self.assertRaises(ProductNotFoundError):
            self.inventory.get_product(999)

    def test_add_duplicate_product_raises(self):
        self.inventory.add_product(self.product)
        with self.assertRaises(ProductAlreadyExistsError):
            self.inventory.add_product(self.product)

    def test_update_quantity(self):
        self.inventory.add_product(self.product)
        self.inventory.update_quantity(1, 5)
        self.assertEqual(self.inventory.get_product(1).quantity, 5)

    def test_update_price(self):
        self.inventory.add_product(self.product)
        self.inventory.update_price(1, 5.5)
        self.assertEqual(self.inventory.get_product(1).price, 5.5)

    def test_total_value(self):
        self.inventory.add_product(self.product)
        self.assertEqual(self.inventory.total_value(), 1500.0)

    def test_below_stock(self):
        self.inventory.add_product(Product(2, "Mouse", 50.0, 3))
        self.assertEqual(len(self.inventory.list_below_stock(5)), 1)

if __name__ == "__main__":
    unittest.main()
