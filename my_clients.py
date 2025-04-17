import os
from splash_screen import show_splash_screen
import tkinter as tk


class MainApp:
    # Класс для управления ресурсами и поведением приложения
    def __init__(self, root):
        self.root = root
        self.root.title("My clients")
        self.root.geometry("500x500+500+150")

        # Установка иконки приложения
        self.set_icon()

        # Отрисовка интерфейса
        self.render_ui()

    def set_icon(self):
        # Метод для установки иконки виджета
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "resources",
            "icon.ico"
        )
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

    def render_ui(self):
        # Скоро здесь будут методы для отрисовки интерфейса
        pass


def start_main_app(splash):
    # Функция для запуска основного окна
    splash.destroy()  # Закрыть окно заставки
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    show_splash_screen(start_main_app, "Добро пожаловать", "Дарья")
