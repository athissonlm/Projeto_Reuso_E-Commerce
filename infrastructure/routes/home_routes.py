"""Rota inicial da aplicação.
Este módulo expõe a página principal do framework como catálogo do e-commerce.
"""

from flask import Blueprint, render_template

from backend.services.catalog.service import CatalogService

home_bp = Blueprint('home_bp', __name__)
service = CatalogService()


@home_bp.route('/', endpoint='home')
def home():
    produtos = service.list_products()
    return render_template('homepage.html', produtos=produtos, total=len(produtos))
