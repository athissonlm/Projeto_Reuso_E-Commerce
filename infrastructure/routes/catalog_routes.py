"""Rota do catálogo.
Este módulo conecta as páginas de catálogo e detalhe do produto ao serviço de catálogo.
"""

from flask import Blueprint, render_template, request

from backend.services.catalog.service import CatalogService

catalog_bp = Blueprint('catalog_bp', __name__)
service = CatalogService()


@catalog_bp.route('/catalog', endpoint='catalog_home')
def catalog_home():
    return products()


@catalog_bp.route('/catalog/products', endpoint='products')
@catalog_bp.route('/products', endpoint='products_legacy')
def products():
    q = request.args.get('q', '').strip()
    metodo = request.args.get('metodo', 'linear')
    ordenacao = request.args.get('ordenacao', 'price_asc')
    resultados = service.list_products(q=q, metodo=metodo, ordenacao=ordenacao)

    return render_template(
        'crafts.html',
        produtos=resultados,
        q=q,
        metodo=metodo,
        ordenacao=ordenacao,
        total=len(resultados)
    )


@catalog_bp.route('/catalog/product/<product_name>', endpoint='product_page')
@catalog_bp.route('/product/<product_name>', endpoint='product_page_legacy')
def product_page(product_name):
    produto = service.get_product_by_name(product_name)
    if not produto:
        return render_template('productpage.html', not_found=True, product_name=product_name)

    return render_template(
        'productpage.html',
        product_name=produto.get('name', ''),
        product_img=produto.get('img', ''),
        product_desc=produto.get('description', 'Produto comercial com qualidade e atendimento confiável.'),
        product_price=produto.get('price', 0.0),
        not_found=False
    )
