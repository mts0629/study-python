import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import BaseRequestHandler
from typing import Any, Callable

# HTML string
page_str = """
<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Server test</h1>
    <p>Hello, world!</p>
</body>
</html>
"""


class MyRequestHandler(BaseHTTPRequestHandler):
    """Handler for HTTP requests."""

    def do_GET(self):
        """Actions for GET method: send HTML strings."""
        # Status code
        self.send_response(HTTPStatus.OK)

        # HTTP header
        self.send_header("Content-Type", "text/html; charset=utf-8")
        encoded_str = page_str.encode(encoding="utf-8")
        self.send_header("Content-Length", len(encoded_str))
        self.end_headers()

        # Message body
        self.wfile.write(encoded_str)

    def do_POST(self):
        """Actions for POST method: receive a request."""
        content = f"POST {self.path}"

        self.send_response(HTTPStatus.OK)

        self.send_header("Content-Type", "text/plain; charset=utf-8")
        content = content.encode(encoding="utf-8")
        self.send_header("Content-Length", len(content))
        self.end_headers()

        self.wfile.write(content)


def run_server(
    server_addr: str,
    port: int,
    handler: Callable[[Any, Any, HTTPServer], BaseRequestHandler],
):
    """Run HTTP server."""
    httpd = HTTPServer((server_addr, port), handler)
    httpd.serve_forever()


if __name__ == "__main__":
    try:
        print("Start a server... (terminate with Ctrl-C)")
        run_server("0.0.0.0", 8000, MyRequestHandler)
    except KeyboardInterrupt:
        print("\nTerminated")
        sys.exit()
