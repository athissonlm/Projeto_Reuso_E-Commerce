# Framework para Sistemas de E-commerce

## 1. Introdução
Este projeto foi desenvolvido como uma proposta acadêmica de framework para sistemas de e-commerce, com foco em reutilização de software, organização modular e arquitetura baseada em microservices lógicos. O objetivo principal é demonstrar como um sistema de comércio eletrônico pode ser estruturado em camadas bem definidas, separando responsabilidades e promovendo componentes reutilizáveis.

## 2. Objetivo
O sistema tem como finalidade apresentar um catálogo de produtos, permitir busca e ordenação de itens, além de demonstrar a estrutura de um framework orientado a e-commerce. A arquitetura foi organizada para facilitar a manutenção, a extensão e a compreensão do projeto em contexto acadêmico.

## 3. Arquitetura do sistema
A solução foi pensada como um monólito modular, mas com visão de microservices lógicos. Isso significa que o sistema ainda roda em uma única aplicação, porém com responsabilidades separadas por domínio.

### 3.1 Camadas do projeto
- Camada de apresentação: responsável pelas páginas HTML e rotas visíveis ao usuário.
- Camada de serviços: contém a lógica de negócio, como catálogo e pedidos.
- Camada de repositórios: acessa e manipula os dados dos produtos.
- Camada de componentes reutilizáveis: reúne algoritmos compartilhados, como busca e ordenação.

## 4. Microservices lógicos
O projeto foi organizado para representar os principais domínios de um e-commerce:

### 4.1 Catalog Service
Responsável pela listagem, busca e filtro de produtos.

### 4.2 Order Service
Responsável pela criação de pedidos, cálculo do total e acompanhamento do status.

### 4.3 Cart Service
Representa a lógica de carrinho, incluindo itens e quantidades.

### 4.4 Payment Service
Representa a etapa de checkout e pagamento.

Esses serviços são implementados como módulos lógicos dentro do sistema, o que atende ao objetivo didático sem exigir escalabilidade real no momento.

## 5. Componentes de software reutilizáveis
Entre os principais componentes reutilizáveis presentes no projeto, destacam-se:

- busca linear
- busca binária
- ordenação por bolha
- serviços de catálogo
- serviços de pedidos

Esses elementos podem ser reaproveitados em outras partes do sistema sem duplicação de código.

## 6. Estrutura do projeto

```text
E-Commerce - Reuso de Software/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── factory.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── products.py
│   │   └── orders.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── catalog_service.py
│   │   └── order_service.py
│   └── repositories/
│       ├── __init__.py
│       └── product_repository.py
├── shared/
│   ├── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── search.py
├── static/
│   ├── produtos.json
│   ├── style.css
│   └── img_prod/
├── templates/
│   ├── homepage.html
│   ├── crafts.html
│   └── productpage.html
├── tests/
│   └── test_routes.py
├── main.py
├── models.py
├── views.py
├── requirements.txt
├── readme.md
└── .gitignore
```

## 7. Tecnologias utilizadas
- Python
- Flask
- Jinja2
- Estrutura modular em pacotes
- JSON para armazenamento local de catálogo

## 8. Execução do projeto
Para rodar a aplicação localmente, execute os seguintes passos:

```bash
cd "C:\Users\Athisson Alberto\Documents\Projetos\E-Commerce - Reuso de Software"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

## 9. Conclusão
O projeto demonstrou uma abordagem acadêmica de framework para e-commerce, unindo práticas de reutilização de software, organização por camadas e arquitetura baseada em microservices lógicos. Mesmo sendo uma solução simples, ela apresenta uma base sólida para entendimento de engenharia de software, arquitetura de sistemas e organização modular de aplicações web.
