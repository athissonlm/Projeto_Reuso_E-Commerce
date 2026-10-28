"""Factory da aplicação.
Este módulo centraliza a criação da instância Flask e o registro dos módulos do sistema.
"""

from pathlib import Path

from flask import Flask

from infrastructure.config import Config
from infrastructure.routes.cart_routes import cart_bp
from infrastructure.routes.catalog_routes import catalog_bp
from infrastructure.routes.checkout_routes import checkout_bp
from infrastructure.routes.home_routes import home_bp
from infrastructure.routes.order_routes import order_bp


def create_app():
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(project_root / 'frontend' / 'templates'),
        static_folder=str(project_root / 'frontend' / 'static'),
    )
    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(order_bp)

    return app
