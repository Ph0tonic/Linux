#!/usr/bin/env python

#SOURCE CODE FROM https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class snmpHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        print (self.path)
        if self.path == "/graph.svg":
            #SVG binaire
            #self.send_header('Content-type','image/svg')
            #svgFile = open('graph.svg', 'rb')
            #svg xml
            self.send_header('Content-type','image/svg+xml')
            svgFile = open('graph.svg', 'r')
            self.end_headers()
            self.wfile.write(bytes(svgFile.read(), 'utf8'))
            svgFile.close()
        else :
            self.send_header('Content-type','text/html')
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


def run():
    print('starting server...')

    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, snmpHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
