"""
@ GREGÓRIO HONORATO
PROGRAMA DESENVOLVIDO PARA DEXTRA 05/04/2017
"""
try: from flask import Flask
except: print("INSTALE O PACOTE Flask")
app = Flask(__name__)

class SuperLanchoneteDextra:
    def __init__(self):
        self.carregar_pagina()
        #HABILITA A ATUALIZAÇÃO DO CODIGO PARA O CLIENTE
        app.run(use_reloader=True)

    @app.route("/")
    def carregar_pagina():
        return "CARDAPIO DA SUPER LANCHONETE DA DEXTRA!"

SuperLanchoneteDextra()
