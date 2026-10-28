"""Serviço do catálogo.
Este módulo encapsula a lógica de listagem, filtragem e busca de produtos.
"""

from backend.components.search import bubble_sort, busca_linear, busca_binaria
from backend.repositories.product_repository import ProductRepository


class CatalogService:
    def __init__(self, repository=None):
        self.repository = repository or ProductRepository()

    def list_products(self, q='', metodo='linear', ordenacao='price_asc'):
        base = self.repository.get_all()

        if ordenacao == 'price_asc':
            lista = bubble_sort(base)
        elif ordenacao == 'price_desc':
            lista = bubble_sort(base, reverse=True)
        elif ordenacao == 'name_asc':
            lista = bubble_sort(base, key=lambda x: str(x.get('name', '')).lower())
        elif ordenacao == 'name_desc':
            lista = bubble_sort(base, key=lambda x: str(x.get('name', '')).lower(), reverse=True)
        else:
            lista = base

        if not q:
            return lista

        if metodo == 'binaria':
            resultados = busca_binaria(lista, q)
        else:
            resultados = busca_linear(lista, q)

        return resultados if resultados else []

    def get_product_by_name(self, product_name):
        return self.repository.get_by_name(product_name)
