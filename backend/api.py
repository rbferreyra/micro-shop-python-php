# Product Service

# Importa o framework
from flask import Flask
from flask_restful import Resource, Api

# Instancia a aplicação
app = Flask(__name__)
api = Api(app)

# cria a classe do produto
class Product(Resource):
    def get(self):
        return {
            'products': [
                'Ice cream',
                'Chocolate',
                'Fruit',
                'Food'
            ]
        }

# Cria as rotas
api.add_resource(Product, '/')

# Executa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
