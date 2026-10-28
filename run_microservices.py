"""Orquestrador dos microserviços do framework de e-commerce.
Este módulo inicia em processos separados os serviços de catálogo, carrinho,
checkout e pedidos nas portas definidas pelo projeto.
"""

from multiprocessing import Process

from infrastructure.microservices.catalog_service import create_catalog_app
from infrastructure.microservices.cart_service import create_cart_app
from infrastructure.microservices.checkout_service import create_checkout_app
from infrastructure.microservices.order_service import create_order_app


def run_app(app, host, port):
    app.run(host=host, port=port, debug=True, use_reloader=False)


if __name__ == '__main__':
    processes = [
        Process(target=run_app, args=(create_catalog_app(), '127.0.0.1', 8000)),
        Process(target=run_app, args=(create_cart_app(), '127.0.0.1', 8001)),
        Process(target=run_app, args=(create_checkout_app(), '127.0.0.1', 8002)),
        Process(target=run_app, args=(create_order_app(), '127.0.0.1', 8003)),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
