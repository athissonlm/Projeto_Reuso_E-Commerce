"""Microserviço de pedidos.
Este módulo expõe o histórico e a criação de pedidos como aplicação Flask independente na porta 8003.
"""

from pathlib import Path

from flask import Flask

from infrastructure.routes.order_routes import order_bp


def create_order_app():
    project_root = Path(__file__).resolve().parents[2]
    app = Flask(
        __name__,
        template_folder=str(project_root / 'frontend' / 'templates'),
        static_folder=str(project_root / 'frontend' / 'static'),
    )
    app.register_blueprint(order_bp)
    return app
