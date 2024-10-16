# forma mais simples de criar api com python é o flask
from flask import Flask, jsonify, request

crud_api = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'It : A coisa',
        'autor': 'Stephen King'
    },
    {
        'id': 2,
        'titulo': 'O colecionador ',
        'autor': 'John Fowles'
    },
    {
        'id': 3,
        'titulo': 'Harry Potter',
        'autor': 'J.K. Rowling'
    }
]
# Consultar todos os livros
@crud_api.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar apenas um livro específico
@crud_api.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@crud_api.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar novo livro
@crud_api.route('/livros', methods=['POST'])
def incluir_novo_livro(id):
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Excluir Livro
@crud_api.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

crud_api.run(port=5000, host='localhost', debug=True)



