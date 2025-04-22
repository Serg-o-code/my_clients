import tkinter as tk
from typing import Callable


def render_add_client_screen_ui(
        container, 
        return_home_screen_func: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса экрана добавления клиента
    screen_frame = tk.Frame(container)

    title_label = tk.Label(
        screen_frame,
        text="Добавление нового клиента",
        padx=10,
        pady=10,
        font=("Arial", 14, "bold")
    )
    title_label.pack(expand=True)

    return_button = tk.Button(
        screen_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_home_screen_func
    )
    return_button.pack(pady=30)

    return screen_frame
