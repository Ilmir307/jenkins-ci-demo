"""Простое веб-приложение на Python (демо для Jenkins CI, задание 1710)."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    """Отвечает 'Hello, World!' на любой GET-запрос."""

    def do_GET(self):
        """Отправляет текстовый ответ Hello, World!"""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello, World!".encode("utf-8"))


def main():
    """Запускает веб-сервер на порту 8000."""
    server = HTTPServer(("127.0.0.1", 8000), HelloHandler)
    print("Сервер запущен: http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
