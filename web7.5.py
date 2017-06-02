#!/usr/bin/env python3
#!/usr/bin/env python

# Description : Serveur web qui permet de renvoyer une page html
#               avec un graphique d'un fichier svg
# Auteurs : Lucas Bulloni, Malik Fleury et Bastien Wermeille
# Date : 02.06.2017
# Version : 1.0

#SOURCE CODE FROM https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class snmpHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET , reecriture de la fonction de l'objet BaseHTTPRequestHandler
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        if self.path == "/graph.svg":
            #svg xml envoie du contenu du fichier
            self.send_header('Content-type','image/svg+xml')
            svgFile = open('graph.svg', 'r')
            self.end_headers()
            self.wfile.write(bytes(svgFile.read(), 'utf8'))
            svgFile.close()
        else :
            #envoie du text si c'est une autre page que l'image qui est demande
            self.send_header('Content-type','text/html')
            #code HTML
            message = '''<!DOCTYPE html>
                <html>
                <head>
                <title>Nombre de paquets envoy&eacute;s au temps t</title>
                </head>
                <body>
                <h1>Nombre de paquets envoy&eacute;s au temps t</h1>
                <p><object data="/graph.svg" type="image/svg+xml">
                </object>
                </p>
                </body>
                </html>'''
            self.end_headers()
            self.wfile.write(bytes(message, 'utf8'))

        # Write content as utf-8 data

        return

#fonction du demarrage du server web - REQUIERT DROIT SUDO CAR PORT 80
def run():
    print('starting server...')

    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, snmpHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

#demarrage du server
run()
