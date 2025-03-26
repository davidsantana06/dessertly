import webview
from . import app


if __name__ == "__main__":
    webview.create_window("Dessertly", app, min_size=(1280, 720))
    webview.start()
