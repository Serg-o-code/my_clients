import os
from GUI.splash_screen import show_splash_screen
import tkinter as tk
from GUI.home_screen import render_home_screen_ui as rhs_ui
from GUI.add_client_screen import render_add_client_screen_ui as racs_ui
from GUI.client_list_screen import render_client_list_screen_ui as rcls_ui
from GUI.add_client_form_screen import render_add_client_form_screen_ui as racfs_ui


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
            show_add_client_screen=self.show_add_client_screen,
            show_client_list_screen=self.show_client_list_screen
        )
        self.add_client_screen_frame = racs_ui(
            self.root,
            show_add_client_form_screen=self.show_add_client_form_screen,
            return_home_screen=self.show_home_screen
        )

        self.client_list_screen_frame = rcls_ui(
            self.root,
            return_home_screen=self.show_home_screen
        )

        self.add_client_form_screen_frame = racfs_ui(
            self.root,
            return_add_client_screen=self.show_add_client_screen
        )

        self.show_home_screen()

    def show_home_screen(self) -> None:
        self.add_client_screen_frame.pack_forget()
        self.client_list_screen_frame.pack_forget()
        self.add_client_form_screen_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def show_add_client_screen(self) -> None:
        self.home_frame.pack_forget()
        self.client_list_screen_frame.pack_forget()
        self.add_client_form_screen_frame.pack_forget()
        self.add_client_screen_frame.pack(fill="both", expand=True)

    def show_client_list_screen(self) -> None:
        self.home_frame.pack_forget()
        self.add_client_screen_frame.pack_forget()
        self.add_client_form_screen_frame.pack_forget()

        # Если был старый фрейм — убираем
        if hasattr(self, 'client_list_screen_frame'):
            self.client_list_screen_frame.destroy()

         # Пересоздаем с актуальными данными
        self.client_list_screen_frame = rcls_ui(
        self.root,
        return_home_screen=self.show_home_screen
        )
        self.client_list_screen_frame.pack(fill="both", expand=True)

    
    def show_add_client_form_screen(self) -> None:
        self.add_client_screen_frame.pack_forget()
        self.add_client_form_screen_frame.pack(fill="both", expand=True)

    def set_icon(self) -> None:
        # Метод для установки иконки виджета
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "resources",
            "icon.ico"
        )
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)


def start_main_app(splash):
    # Функция для запуска основного окна
    splash.destroy()  # Закрыть окно заставки
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    show_splash_screen(start_main_app)
