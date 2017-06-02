#!/usr/bin/env python

#SOURCE CODE FROM https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class snmpHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        #changer en SVG
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, snmpHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()



'''
Données à retourner, soit SVG

<svg version="1.1"
baseprofile="full"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:ev="http://www.w3.org/2001/xml-events">
<circle cx="50" cy="50" r="40" stroke="green" stroke-width="4"
fill="yellow" />
</svg>


Sinon retourner l’HTML suivant, qui réfère le chemin du SVG ci-dessus :


<!DOCTYPE html>
<html>
<head>
<title>Graphe</title>
</head>
<body>
<h1>Graphe</h1>
<p><object data="/graph.svg" type="image/svg+xml">
</object>
</p>
</body>
</html>

'''
