from http.server import BaseHTTPRequestHandler, HTTPServer
import json

products = [
    { 'name': 'Headphones', 'stock': 50, 'price': 200},
    { 'name': 'Computer', 'stock': 10, 'price': 1000},
    { 'name': 'Pen', 'stock': 100, 'price': 5},
]

class RESTAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Received a GET request!')
        
        path_segments = self.path.split('/')

        if path_segments[1] == 'products':
            if len(path_segments) == 2:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(products).encode())
            else:
                product = next((product for product in products if product['name'] == path_segments[2]))
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(product).encode())

    def do_POST(self):
        print('Received a POST request!')

    def do_PUT(self):
        print('Received a PUT request!')

    def do_DELETE(self):
        print('Received a DELETE request!')

        path_segments = self.path.split('/')

        if path_segments[1] == 'products':
            product = next((product for product in products if product['name'] == path_segments[2]))
            self.send_response(200)
            self.end_headers()
            for x in range(0, len(products)):
                if products[x]['name'] == product['name']:
                    del products[x]
                    break

server = HTTPServer(('localhost', 8000), RESTAPIHandler)
print('Server is listening on localhost:8000')
server.serve_forever()