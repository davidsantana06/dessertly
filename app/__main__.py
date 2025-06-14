import platform
import webview
from . import app


def run_in_windows():
    webview.create_window("Dessertly", app, min_size=(1280, 720))
    webview.start()


def run_in_other_systems():
    app.run()


if __name__ == "__main__":
    is_windows_system = platform.system() == "Windows"
    runner = run_in_windows if is_windows_system else run_in_other_systems
    runner()
