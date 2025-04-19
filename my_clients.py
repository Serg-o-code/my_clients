import os
from splash_screen import show_splash_screen
import tkinter as tk
from home_screen import render_home_screen_ui as rhs_ui
from add_client_screen import render_add_client_screen_ui as racs_ui


class MainApp:
    # Класс для управления ресурсами и поведением приложения
    def __init__(self, root):
        self.root = root
        self.root.title("My clients")
        self.root.geometry("500x500+500+150")
        self.set_icon()

        # Инициализация фреймов
        self.home_frame = rhs_ui(
            self.root,
            add_client_func=self.add_client_screen
        )
        self.screen_frame = racs_ui(
            self.root,
            return_home_screen_func=self.show_home_screen
        )

        self.show_home_screen()

    def set_icon(self) -> None:
        # Метод для установки иконки виджета
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "resources",
            "icon.ico"
        )
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

    def show_home_screen(self) -> None:
        self.screen_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def add_client_screen(self) -> None:
        self.home_frame.pack_forget()
        self.screen_frame.pack(fill="both", expand=True)


def start_main_app(splash):
    # Функция для запуска основного окна
    splash.destroy()  # Закрыть окно заставки
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    show_splash_screen(start_main_app)
