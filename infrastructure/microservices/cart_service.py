"""Microserviço de carrinho.
Este módulo expõe o carrinho como aplicação Flask independente na porta 8001.
"""

from pathlib import Path

from flask import Flask

from infrastructure.routes.cart_routes import cart_bp


def create_cart_app():
    project_root = Path(__file__).resolve().parents[2]
    app = Flask(
        __name__,
        template_folder=str(project_root / 'frontend' / 'templates'),
        static_folder=str(project_root / 'frontend' / 'static'),
    )
    app.register_blueprint(cart_bp)
    return app
