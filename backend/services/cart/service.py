"""Serviço do carrinho.
Este módulo controla os itens adicionados ao carrinho e sua contagem.
"""


class CartService:
    def __init__(self):
        self.items = []

    def add_item(self, product_name, quantity=1):
        if not product_name:
            raise ValueError('Produto é obrigatório.')

        quantity = max(int(quantity), 1)

        for item in self.items:
            if item['name'] == product_name:
                item['quantity'] += quantity
                return item

        self.items.append({'name': product_name, 'quantity': quantity})
        return self.items[-1]

    def get_items(self):
        return self.items

    def get_total(self):
        return sum(item.get('quantity', 0) for item in self.items)
