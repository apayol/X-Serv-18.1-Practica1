#!/usr/bin/python3

"""
Práctica 1: Web acortadora de URLs

Adrián Payol Montero
"""

import webapp
import csv
import os.path
from urllib.parse import unquote

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
        peticion = request.split('=')[-1]
        return (metodo, recurso, peticion)

    def process(self, parsedRequest):
        metodo, recurso, url_orig = parsedRequest
        if (metodo == "GET"):
            print("Es un get")
            if recurso == "favicon.ico":
                codigo = "HTTP/1.1 404 Not Found"
                respuesta_html = "<html><body><h1>Not found</h1></body></html>"
            elif recurso == "/":
                codigo = "HTTP/1.1 200 OK"
                respuesta_html = FORMULARIO + "<html><body>" + str(self.url_corta) + "</html></body>" 
            else:
                codigo = "HTTP/1.1 404 Not Found"
                respuesta_html = "<html><body><h1>Not found</h1></body></html>"
        elif (metodo == "POST"):
            if url_orig == "":
                codigo = "HTTP/1.1 204 No Content"
                respuesta_html = ("<html><body><h1>Formulario sin contenido</h1></body></html>")
            elif (url_orig[0:7] == "http://" or url_orig[0:8] == "https://"):
                url_orig = unquote(url_orig)
            else: #si hay contenido y no empieza por http:// o https://
                url_orig = "http://" + url_orig
   
            self.cont = len(self.url_orig)
            if  url_orig in self.url_orig:
                path = str(self.urrl_orig[url_orig])
                path = "http://localhost:1234/" + path
                codigo = "HTTP/1.1 200 OK"
                respuesta_html = ("<html><body><a href=" + path + ">" + path + "</a></body></html>")
            else:
                self.url_orig[url_orig] = self.cont
                path = "http://localhost:1234/" + str(self.cont)
                self.url_corta[self.cont] = url_orig
                self.cont = self.cont + 1
                codigo = "HTTP/1.1 200 OK"
                respuesta_html = ("<html><body><a href=" + path + ">" + path + "</a></body></html>")
        else:
            codigo = "HTTP/1.1 405 Method Not allowed"
            respuesta_html = ("<html><body><h1>Metodo no permitido" +
                              "</h1></body></html>")
        return (codigo, respuesta_html)

if __name__=="__main__":
    testWebApp = practica1("localhost", 1234)
