from typing import Dict, List, Union
from .models import Product
from .exceptions import ProductAlreadyExistsError, ProductNotFoundError


class Inventory:
    
    def __init__(self):
        self._products: Dict[str, Product] = {}
    
    @staticmethod
    def _validate_non_negative_quantity(quantity: Union[int, float]) -> None:
        
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

    def add_product(self, product: Product) -> None:
        
        if self._products.get(str(product.id)):
            raise ProductAlreadyExistsError(f"Produto '{product.id}' já existe.")
        
        self._validate_non_negative_quantity(product.quantity)
        self._validate_non_negative_quantity(product.quantity)
        self._products[str(product.id)] = product

    def get_product(self, product_id: int) -> Product:
        product = self._products.get(str(product_id))
        
        if not product:
            raise ProductNotFoundError(f"Produto '{product_id}' não encontrado.")
        
        return product

    def update_quantity(self, product_id: int, quantity: int) -> None:

        old_product = self.get_product(product_id)
        self._validate_non_negative_quantity(quantity)
        self._products[str(product_id)] = Product(
            id=old_product.id,
            name=old_product.name,
            price=old_product.price,
            quantity=quantity
        )

    def update_price(self, product_id: int, price: float) -> None:

        old_product = self.get_product(product_id)
        self._validate_non_negative_quantity(price)
        self._products[str(product_id)] = Product(
            id=old_product.id,
            name=old_product.name,
            price=price,
            quantity=old_product.quantity
        )

    def total_value(self) -> float:
        return sum(p.price * p.quantity for p in self._products.values())

    def list_below_stock(self, minimum: int) -> List[Product]:
        return [p for p in self._products.values() if p.quantity < minimum]
