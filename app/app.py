import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Request HTTP Method: GET\n', 'utf-8'))
        logging.info(f'Request HTTP Method: GET')

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Request HTTP Method: POST\n', 'utf-8'))
        logging.info(f'Request HTTP Method: POST')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Allow', 'GET, POST, OPTIONS')
        self.end_headers()
        logging.info(f'Request HTTP Method: OPTIONS')

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        logging.info(f'Request HTTP Method: HEAD')

    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Request HTTP Method: PUT\n', 'utf-8'))
        logging.info(f'Request HTTP Method: PUT')

    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Request HTTP Method: DELETE\n', 'utf-8'))
        logging.info(f'Request HTTP Method: DELETE')

    def do_PATCH(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Request HTTP Method: PATCH\n', 'utf-8'))
        logging.info(f'Request HTTP Method: PATCH')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()