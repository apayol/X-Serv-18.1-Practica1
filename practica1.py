#!/usr/bin/python3

"""
Práctica 1: Web acortadora de URLs

Adrián Payol Montero
"""

import webapp
#import csv

FORMULARIO = """
    <form action="" method="POST">
        Introduzca URL para reducir:<br>
        <input type="text" name="URL" value="http://"><br> 
        <input type="submit" value="Enviar">
    </form> 
"""

url_original = {}
url_corta = {}

class practica1(webapp.webApp):

    def parse(self,request):
        metodo = request.split()[0]
        recurso = request.split()[1]
        return (metodo, recurso, peticion)

    def process(self, parsedRequest):
        metodo, recurso, peticion = parsedRequest
        return (codigo, respuesta_html)

if __name__=="__main__":
    testWebApp = practica1("localhost", 1234)
