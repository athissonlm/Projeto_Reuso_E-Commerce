"""Rota do carrinho.
Este módulo gerencia a visualização e o acréscimo de itens no carrinho de compras.
"""

from flask import Blueprint, redirect, render_template, request, url_for

from backend.services.cart.service import CartService

cart_bp = Blueprint('cart_bp', __name__)
cart_service = CartService()


@cart_bp.route('/cart', methods=['GET'], endpoint='cart')
def cart():
    items = cart_service.get_items()
    total_items = cart_service.get_total()
    return render_template('cart.html', items=items, total_items=total_items)


@cart_bp.route('/cart/add', methods=['POST'], endpoint='add_to_cart')
def add_to_cart():
    product_name = (request.form.get('product_name') or '').strip()
    quantity = int(request.form.get('quantity', 1) or 1)

    if not product_name:
        return redirect(url_for('catalog_bp.products'))

    cart_service.add_item(product_name, quantity)
    return redirect(url_for('cart_bp.cart'))
