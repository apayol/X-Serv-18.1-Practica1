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
    url_cortas = {}
    cont = 0

    def leer(self):
        if os.path.isfile('coleccion_urls.csv'):
            with open('coleccion_urls.csv', 'r') as csvfile:
                leer = csv.reader(csvfile, delimiter = ',')
                for row in leer:
                    self.url_orig[row[0]] = row[1]
                    self.url_cortas[row[1]] = row[0]
                    self.cont = self.cont + 1

    def escribir(self):
        with open('coleccion_urls.csv', 'w', newline='') as csvfile:
            escribir = csv.writer(csvfile, delimiter=',')
            for entrada in self.url_orig:
                escribir.writerow([entrada, self.url_orig[entrada]])
        

    def parse(self,request):
        self.leer()
        metodo = request.split(' ', 1)[0]
        recurso = request.split(' ', 2)[1]
        peticion = request.split('=')[-1]
        return (metodo, recurso, peticion)

    def process(self, parsedRequest):
        metodo, recurso, url_orig = parsedRequest

        if (metodo == "GET"):
            if recurso == "favicon.ico":
                codigo = "HTTP/1.1 404 Not Found"
                respuesta_html = "<html><body><h1>Not found</h1></body></html>"
            elif recurso == "/":
                codigo = "HTTP/1.1 200 OK"
                respuesta_html = (FORMULARIO + "<html><body>Mi lista de URLs acortadas:" +
                                  str(self.url_cortas) + "</html></body>")
            else:
                recurso = recurso[1:]
                if recurso in self.url_cortas:
                    codigo = "HTTP/1.1 302 Redirect" #Redirección en 0s
                    respuesta_html = ("<html><meta http-equiv='Refresh' content= 0;url=" + 
                                      self.url_cortas[recurso] + "></p></body></html>") 
                else:
                    codigo = "HTTP/1.1 404 Not Found"
                    respuesta_html = "<html><body><h1>Not found!</h1></body></html>"

        elif (metodo == "POST"):
            if url_orig == "": #formulario vacío
                codigo = "HTTP/1.1 204 No Content"
                respuesta_html = ("<html><body><h1>Formulario sin contenido</h1></body></html>")
            else: #dicotomía http
                if (url_orig[0:13] == "http%3A%2F%2F" or url_orig[0:14] == "https%3A%2F%2F"):
                    from urllib.parse import unquote
                    url_orig = unquote(url_orig)
                else: 
                    url_orig = "http://" + url_orig
   
                self.cont = len(self.url_orig)
                if  url_orig in self.url_orig: #entrada ya existente
                    path = "http://localhost:1234/" + str(self.url_orig[url_orig])
                    codigo = "HTTP/1.1 200 OK"
                    respuesta_html = ("<html><body>La URL corta es: <a href=" + path + ">" +
                                      path + "</a><br/>La original es: <a href=" + url_orig + ">" +
                                      url_orig + "</a></body></html>")
                else: #nueva entrada
                    self.url_orig[url_orig] = self.cont
                    path = "http://localhost:1234/" + str(self.cont)
                    self.url_cortas[self.cont] = url_orig
                    self.cont = self.cont + 1
                    self.escribir()
                    codigo = "HTTP/1.1 200 OK"
                    respuesta_html = ("<html><body>Nueva URL corta creada: <a href=" + path + ">" +
                                      path + "</a><br/>La original es: <a href=" + url_orig + ">" +
                                      url_orig + "</a></body></html>")
        else:
            codigo = "HTTP/1.1 405 Method Not allowed"
            respuesta_html = ("<html><body><h1>Metodo no permitido</h1></body></html>")
        return (codigo, respuesta_html)

if __name__=="__main__":
    testWebApp = practica1("localhost", 1234)
