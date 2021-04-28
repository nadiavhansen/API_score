# Exercício 1
# Pessoa:
# Será cadastrada previamente (pelo dev) com Nome, Cpf, Dívida, Score e Data de nascimento.
# A dívida de ser um valor em reais entre 0 ao +infinito (podendo ser com até duas casas decimais).
# O score deverá ser um número de 0 até 1000, porém caso haja alguma dívida ativa, ela deverá ser menor de 1000.
# A pessoa poderá ter apenas uma única dívida, que quando paga, deverá ficar salva com o valor R$0,00. | 0.0 no banco.
#
#
# Serasa:
# Terá acesso acesso as informações (Nome, Dívida, Score) de todas as pessoas maiores de 18 anos cadastradas
# Deverá ter uma rota para a pessoa requisitar o seu score e a sua dívida.
# Deverá ter uma rota para a pessoa pagar sua dívida. (A dívida não poderá ser paga parcelada ou apenas uma parte dela,
# terá que ser a vista)
# Quando a dívida for paga o score deverá aumentar até o máximo (1000)

import MySQLdb
from flask import Flask, request
import json
import pandas as pd
import datetime

conn = MySQLdb.connect(host="localhost", user="root", db="ex_serasa", port=3306)
conn.autocommit(True)
cursor = conn.cursor()

app = Flask(__name__)

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


@app.route("/acessar_informacoes/", methods=["GET"])
def acessar_informacoes():

    sql = f"SELECT * FROM cadastro "
    cursor.execute(sql)
    columns = [i[0] for i in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)

    df["Nascimento"] = pd.to_datetime(df["Nascimento"])
    df = df.loc[df["Nascimento"].apply(calculate_age) >= 18]

    df = df.drop(["Cpf", "Nascimento"], axis=1)
    json = df.to_json(orient="records")

    return json


# Deverá ter uma rota para a pessoa requisitar o seu score e a sua dívida.
@app.route("/consultar_score/<Cpf>", methods=["GET"])
def consultar_score_e_divida(Cpf=None):

    sql = f"SELECT Score, Divida FROM cadastro "
    if id:
        sql += f"WHERE Cpf = {Cpf}"

    cursor.execute(sql)
    columns = [i[0] for i in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    json = df.to_json(orient="records")

    return json

# Deverá ter uma rota para a pessoa pagar sua dívida. (A dívida não poderá ser paga parcelada ou apenas uma parte dela,
# terá que ser a vista)


@app.route("/pagar_divida/<Cpf>", methods=["PUT"])
def pagar_divida(Cpf=None):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    sql = f"""SELECT Divida FROM cadastro WHERE Cpf = '{Cpf}'"""
    cursor.execute(sql)

    divida_atual = 0
    for i in cursor.fetchall():
        divida_atual = i[0]

    try:
        if divida_atual == dict_values['Divida']:
            print("entrou no if")
            sql = f"""UPDATE cadastro SET
                    Divida = 0,
                    Score = 1000
                    WHERE Cpf = '{Cpf}'"""
            print(sql)
            affected_rows = cursor.execute(sql)
            if affected_rows > 0:

                return "Divida quitada!"

    except Exception as error:
        return str(error.args)


if __name__ == "__main__":
    app.run(debug=True)
