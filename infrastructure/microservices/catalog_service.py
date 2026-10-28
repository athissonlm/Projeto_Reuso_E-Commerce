"""Microserviço de catálogo.
Este módulo expõe o catálogo como aplicação Flask independente na porta 8000.
"""

from pathlib import Path

from flask import Flask

from infrastructure.routes.catalog_routes import catalog_bp


def create_catalog_app():
    project_root = Path(__file__).resolve().parents[2]
    app = Flask(
        __name__,
        template_folder=str(project_root / 'frontend' / 'templates'),
        static_folder=str(project_root / 'frontend' / 'static'),
    )
    app.register_blueprint(catalog_bp)
    return app
