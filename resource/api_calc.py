from flask_restful import Resource, reqparse

class Calculator_sum(Resource):
    dados = reqparse.RequestParser()
    dados.add_argument('num1', type=str)
    dados.add_argument('num2', type=str)

    def post(self):
        dados = dict(Calculator_sum.dados.parse_args())
        num1 = dados['num1']
        num2 = dados['num2']
        sum = float(num1) + float(num2)        
        return {'status' : 'OK', 'sum' : sum}