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

@crud_api.route('/')
def obter_livros():
    return jsonify(livros)
crud_api.run(port=5000, host='localhost', debug=True)
# Consultar apenas um livro específico
# Editar
# Excluir
