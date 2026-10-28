"""Componentes reutilizáveis de busca e ordenação.
Este módulo fornece algoritmos genéricos para catálogo, filtros e organização dos dados.
"""


def bubble_sort(lista, key=None, reverse=False):
    if key is None:
        if lista and isinstance(lista[0], dict) and 'price' in lista[0]:
            key = lambda x: float(x.get('price', 0) or 0)
        else:
            key = lambda x: x

    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            a = key(lista[j])
            b = key(lista[j + 1])
            if (a > b and not reverse) or (a < b and reverse):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista


def busca_linear(lista, termo, field='name'):
    termo = str(termo or '').strip().lower()
    if not termo:
        return []

    resultados = []
    for item in lista:
        valor = str(item.get(field, '')).strip().lower()
        if termo in valor:
            resultados.append(item)
    return resultados


def busca_binaria(lista, termo, field='name'):
    termo = str(termo or '').strip().lower()
    if not termo:
        return []

    ordenada = bubble_sort(list(lista), key=lambda x: str(x.get(field, '')).strip().lower())
    nomes = [str(x.get(field, '')).strip().lower() for x in ordenada]
    n = len(nomes)
    if n == 0:
        return []

    esquerda, direita = 0, n
    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if nomes[meio] < termo:
            esquerda = meio + 1
        else:
            direita = meio

    resultados = []
    indice = esquerda
    while indice < n and nomes[indice].startswith(termo):
        resultados.append(ordenada[indice])
        indice += 1

    if resultados:
        return resultados

    return busca_linear(lista, termo, field=field)
