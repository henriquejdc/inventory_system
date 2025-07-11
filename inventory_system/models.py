from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    price: float
    quantity: int
