import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Conexion exitosa a la base de datos</h1>")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Backend corriendo en el puerto {PORT}")
    httpd.serve_forever()