"""Serviço de checkout.
Este módulo calcula o total de uma compra com base nos itens do pedido.
"""

from backend.repositories.product_repository import ProductRepository


class CheckoutService:
    def __init__(self, repository=None):
        self.repository = repository or ProductRepository()

    def calculate_total(self, items):
        total = 0.0
        for item in items:
            product = self.repository.get_by_name(item.get('name'))
            if not product:
                raise ValueError(f"Produto não encontrado: {item.get('name')}")
            total += float(product.get('price', 0)) * float(item.get('quantity', 1))
        return round(total, 2)
