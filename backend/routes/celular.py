import json

from flask import Flask, request, jsonify

from models.parametros_busca_celular import ParametrosBuscaCelulares
from services.buscar_celulares import buscar_celulares

app = Flask(__name__)


@app.route('/buscar-celulares', methods=["POST"])
def tratar_busca_celular():
    data = request.get_json()

    parametros_da_busca = ParametrosBuscaCelulares(**data)

    resultado = buscar_celulares(parametros_da_busca)

    return jsonify(resultado)

