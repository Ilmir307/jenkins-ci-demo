"""Модульный тест веб-приложения app.py (задание 1710)."""

import threading
import unittest
import urllib.request

from app import HTTPServer, HelloHandler


class AppTestCase(unittest.TestCase):
    """Проверяет ответ сервера на GET-запрос."""

    def test_hello(self):
        """Сервер на случайном порту отвечает 'Hello, World!' с кодом 200."""
        server = HTTPServer(("127.0.0.1", 0), HelloHandler)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        try:
            with urllib.request.urlopen(
                    "http://127.0.0.1:" + str(port) + "/") as response:
                body = response.read().decode("utf-8")
            self.assertEqual(body, "Hello, World!")
            self.assertEqual(response.status, 200)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
