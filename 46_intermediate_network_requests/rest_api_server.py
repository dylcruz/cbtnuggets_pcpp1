from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse

products = [
    { 'name': 'Headphones', 'stock': 50, 'price': 200},
    { 'name': 'Computer', 'stock': 10, 'price': 1000},
    { 'name': 'Pen', 'stock': 100, 'price': 5},
]

class RESTAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):        
        path_segments = urllib.parse.urlparse(self.path).path.split('/')

        if path_segments[1] == 'products':
            if len(path_segments) == 2:
                params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                name_filter = params.get('name', [''])[0]

                if len(name_filter) > 0:
                    response_data = json.dumps(
                        [p for p in products if name_filter in p['name']]
                    ).encode()
                else:
                    response_data = json.dumps(products).encode()
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(response_data))
                self.end_headers()
                self.wfile.write(response_data)
            else:
                product = next((product for product in products if product['name'] == path_segments[2]))
                response_data = json.dumps(product).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(response_data))
                self.end_headers()
                self.wfile.write(response_data)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length)
        new_product = json.loads(request_data.decode())
        products.append(new_product)
        self.send_response(201)
        self.end_headers()

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length)
        product_update_data = json.loads(request_data.decode())

        path_segments = self.path.split('/')
        if path_segments[1] == 'products':
            product = next((product for product in products if product['name'] == path_segments[2]))
            self.send_response(201)
            self.end_headers()
            product[product_update_data['update_value']] = product_update_data['new_value']
            return

    def do_DELETE(self):
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