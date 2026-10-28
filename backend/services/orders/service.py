"""Serviço de pedidos.
Este módulo cria e gerencia pedidos do sistema de e-commerce.
"""

from backend.repositories.product_repository import ProductRepository


class OrderService:
    def __init__(self, repository=None):
        self.repository = repository or ProductRepository()

    def create_order(self, customer_name, items):
        if not customer_name or not items:
            raise ValueError('Cliente e itens do pedido são obrigatórios.')

        total = 0.0
        for item in items:
            product = self.repository.get_by_name(item.get('name'))
            if not product:
                raise ValueError(f"Produto não encontrado: {item.get('name')}")
            total += float(product.get('price', 0)) * float(item.get('quantity', 1))

        return {
            'customer': customer_name,
            'items': items,
            'total': round(total, 2),
            'status': 'created'
        }

    def get_order_status(self, order):
        return order.get('status', 'created')
