#!/usr/bin/python3

"""
Práctica 1: Web acortadora de URLs

Adrián Payol Montero
"""

import webapp
import csv
import os.path

FORMULARIO = """
    <form action="" method="POST">
        Introduzca URL para reducir:<br>
        <input type="text" name="URL" value="http://"><br>
        <input type="submit" value="Enviar">
    </form> 
"""

class practica1(webapp.webApp):

    url_orig = {}
    url_corta = {}

    def leer(self):
        if os.path.isfile('coleccion_urls.csv'):
            with open('coleccion_urls.csv', 'r') as csvfile:
                leer = csv.reader(csvfile, delimiter = ',')
                for row in read:
                    self.url_orig[row[0]] = row[1]
                    self.url_corta[row[1]] = row[0]
            self.url_n = len(self.url_orig)
        else:
            self.url_n = 0

    def escribir(self):
        with open('coleccion_urls.csv', 'w', newline='') as csvfile:
            escribir = csv.writer(csvfile, delimiter=',')
            for entrada in self.url_orig:
                escribir.writerow([entrada, self.list_urls[entrada]])
        

    def parse(self,request):
        self.leer()
        metodo = request.split(' ', 1)[0]
        recurso = request.split(' ', 2)[1]
        url_orig = request.split('=')[-1]
        print(metodo)
        print(recurso)
        return (metodo, recurso, url_orig)

    def process(self, parsedRequest):
        metodo, recurso, url_orig = parsedRequest
        
        return (codigo, respuesta_html)

if __name__=="__main__":
    testWebApp = practica1("localhost", 1234)
