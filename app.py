from flask import Flask
from flask_restful import Api
from resource.api_calc import Calculator_sum
from resource.page_calc import Calc

app = Flask(__name__)
api = Api(app)

api.add_resource(Calculator_sum, '/sum')
app.add_url_rule('/', view_func=Calc.home, methods=['POST','GET'])

if __name__ == '__main__':
    app.run(host='localhost', port=8080 , debug=True)