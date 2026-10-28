"""Microserviço de checkout.
Este módulo expõe o processo de pagamento como aplicação Flask independente na porta 8002.
"""

from pathlib import Path

from flask import Flask

from infrastructure.routes.checkout_routes import checkout_bp


def create_checkout_app():
    project_root = Path(__file__).resolve().parents[2]
    app = Flask(
        __name__,
        template_folder=str(project_root / 'frontend' / 'templates'),
        static_folder=str(project_root / 'frontend' / 'static'),
    )
    app.register_blueprint(checkout_bp)
    return app
