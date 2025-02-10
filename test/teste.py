import requests


def pegar_requisicao_atual():
    url = 'http://localhost:8080/'

    res = requests.get(url)

    print(res.json())


produto = {
    'id' : 20,
    'nome' : 'Xbox Series S',
    'descricao' : 'Video Game 4k 120 FPS Ultima Geração',
    'preco': 1999.99,
    'estoque' : 12
}

produto_editar = {
    'id' : 7,
    'nome' : 'Controle Xbox Series',
    'descricao' : 'Controle sem fio para Xbox',
    'preco': 349.99,
    'estoque' : 46
}

def adicionar_item(dicionario):

    url = f"http://localhost:8080/produtos/"

    res = requests.post(url = url, json = dicionario)

    print(res)


def remover_item(id):

    url = f'http://localhost:8080/produtos/{id}'

    res = requests.delete(url)

    print(res)


def editar_item(dicionario):

    url = f'http://localhost:8080/produtos/{dicionario['id']}'

    res = requests.put(url= url, json= dicionario)

    print(res)

# adicionar_item(produto)

#remover_item(4)

editar_item(produto_editar)