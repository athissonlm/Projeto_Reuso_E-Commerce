"""Rota de checkout.
Este módulo processa a compra, calcula o valor total e expõe a página de finalização.
"""

from flask import Blueprint, jsonify, render_template, request

from backend.services.checkout.service import CheckoutService

checkout_bp = Blueprint('checkout_bp', __name__)


@checkout_bp.route('/checkout', methods=['GET'], endpoint='checkout_page')
def checkout_page():
    return render_template('checkout.html')


@checkout_bp.route('/checkout', methods=['POST'], endpoint='checkout')
def checkout():
    data = request.get_json(silent=True) or {}
    items = data.get('items', [])

    try:
        service = CheckoutService()
        total = service.calculate_total(items)
        return jsonify({'success': True, 'total': total}), 200
    except ValueError as exc:
        return jsonify({'success': False, 'error': str(exc)}), 400
