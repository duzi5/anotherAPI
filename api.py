from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False





@app.before_first_request
def cria_banco():
    banco.create_all()



@app.route('/')
def index(): 
    return "testando"


def todo_exists(self, todo_id):
    pass



class todo(Resource):
    def get(self, todo_id):
        if not todo_id:
            return('usuário não especificado/encontrado')
        else:
            return todos[todo_id]     

    def delete(self, todo_id):
        pass

        


if __name__ == "__main__":
    from Alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
