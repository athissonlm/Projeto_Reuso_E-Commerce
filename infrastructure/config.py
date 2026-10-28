"""Configuração central da aplicação.
Este arquivo guarda as definições globais de ambiente usadas pelo projeto Flask.
"""


class Config:
    SECRET_KEY = 'ecommerce-framework-secret'
    DEBUG = True
    TESTING = False
    JSON_SORT_KEYS = False
