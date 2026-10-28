"""Repositório de produtos.
Este módulo acessa os dados do catálogo armazenados em arquivo JSON.
"""

import json
from pathlib import Path


class ProductRepository:
    def __init__(self, file_path=None):
        base_dir = Path(__file__).resolve().parent.parent
        self.file_path = file_path or base_dir / 'data' / 'produtos.json'

    def get_all(self):
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                data = json.load(file)
            return data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_by_name(self, product_name):
        target = str(product_name or '').strip().lower()
        for item in self.get_all():
            if str(item.get('name', '')).strip().lower() == target:
                return item
        return None
