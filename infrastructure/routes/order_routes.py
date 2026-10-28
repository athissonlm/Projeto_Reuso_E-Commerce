"""Rota de pedidos.
Este módulo expõe operações de criação, consulta e visualização de pedidos do cliente.
"""

from flask import Blueprint, jsonify, render_template, request

from backend.services.orders.service import OrderService

order_bp = Blueprint('order_bp', __name__)


@order_bp.route('/orders', methods=['GET'], endpoint='orders')
def orders():
    return render_template('orders.html')


@order_bp.route('/orders', methods=['POST'], endpoint='create_order')
def create_order():
    data = request.get_json(silent=True) or {}
    customer_name = data.get('customer_name', '').strip()
    items = data.get('items', [])

    try:
        service = OrderService()
        order = service.create_order(customer_name, items)
        return jsonify({'success': True, 'order': order}), 201
    except ValueError as exc:
        return jsonify({'success': False, 'error': str(exc)}), 400


@order_bp.route('/orders/<order_id>', methods=['GET'], endpoint='get_order')
def get_order(order_id):
    return jsonify({
        'success': True,
        'order_id': order_id,
        'status': 'created'
    })
