# import MySQLdb
# from flask import Flask, request
# import json
#
# # Exercício 1
# # Pessoa:
# # Será cadastrada previamente (pelo dev) com Nome, Cpf, Dívida, Score e Data de nascimento.
# # A dívida de ser um valor em reais entre 0 ao +infinito (podendo ser com até duas casas decimais).
# # O score deverá ser um número de 0 até 1000, porém caso haja alguma dívida ativa, ela deverá ser menor de 1000.
# # A pessoa poderá ter apenas uma única dívida, que quando paga, deverá ficar salva com o valor R$0,00. | 0.0 no banco.
# #
# #
# # Serasa:
# # Terá acesso acesso as informações (Nome, Dívida, Score) de todas as pessoas maiores de 18 anos cadastradas
# # Deverá ter uma rota para a pessoa requisitar o seu score e a sua dívida.
# # Deverá ter uma rota para a pessoa pagar sua dívida. (A dívida não poderá ser paga parcelada ou apenas uma parte dela,
# # terá que ser a vista)
# # Quando a dívida for paga o score deverá aumentar até o máximo (1000)
#
#
# class Pessoa:
#
#     conn = MySQLdb.connect(host="localhost", user="root", db="ex_serasa", port=3306)
#     conn.autocommit(True)
#     cursor = conn.cursor()
#
#     app = Flask(__name__)
#
#     def __init__(self, nome: str, cpf: str, divida: float, score: int, data_nascimento: str):
#         self.nome = nome
#         self.cpf = cpf
#         self.divida = divida
#         self.score = score
#         self.data_nascimento = data_nascimento
#
#     def cadastrar(self):
#
#         try:
#             sql = f"""INSERT INTO cadastro VALUES
#                 (default, '{self.nome}', '{self.cpf}', '{self.divida}', '{self.score}', '{self.data_nascimento}')"""
#
#             affected_rows = self.cursor.execute(sql)
#
#             if affected_rows > 0:
#                 return "Sucesso"
#
#         except Exception as error:
#             return error
#
#
# pessoa = Pessoa("Valdir", "10010016", 0, 10000, "18/09/2009")
# pessoa.cadastrar()
#
# # @app.route("/cadastrar/", methods=["POST"])
# # def cadastrar(self):
# #
# #     raw_request = request.data.decode("utf-8")
# #     dict_values = json.loads(raw_request)
# #
# #     try:
# #         sql = f"""INSERT INTO cadastro VALUES
# #             (default,
# #             '{dict_values['Nome']}',
# #             '{dict_values['Cpf']}',
# #             {dict_values['Divida']},
# #             {dict_values['Score']},
# #             {dict_values['Nascimento']})"""
# #
# #         affected_rows = self.cursor.execute(sql)
# #
# #         if affected_rows > 0:
# #             return "Deu tudo certo!", 200
# #
# #     except Exception as error:
# #         return str(error.args)
# #
# #     return "Algo deu errado!", 400
# #
# # if __name__ == "__main__":
# #     app.run(debug=True)
#
#
