"""Ponto de entrada principal do framework de e-commerce.
Este módulo inicia a aplicação Flask e executa o servidor local do sistema.
"""

from infrastructure.app_factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)