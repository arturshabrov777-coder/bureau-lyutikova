"""
Простой веб-сервер для одностраничного сайта «Бюро Лютикова».
Запуск: python app.py
Открыть: http://127.0.0.1:8000
"""

from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8000


class SiteHandler(SimpleHTTPRequestHandler):
    """Отдаём статику из директории проекта."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

    def end_headers(self):
        # Кэш отключаем на время разработки — правки видны сразу
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def run() -> None:
    server = ThreadingHTTPServer((HOST, PORT), SiteHandler)
    print(f"Сервер запущен: http://{HOST}:{PORT}")
    print("Остановка: Ctrl+C")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.server_close()


if __name__ == "__main__":
    run()