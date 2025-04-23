import tkinter as tk
from typing import Callable


def render_client_list_screen_ui(
        container, 
        return_home_screen: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса экрана списка клиентов
    client_list_screen_frame = tk.Frame(container)

    client_list_label = tk.Label(
        client_list_screen_frame,
        text="Список клиентов",
        padx=10,
        pady=10,
        font=("Arial", 14, "bold")
    )
    client_list_label.pack(expand=True)

    back_button = tk.Button(
        client_list_screen_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_home_screen
    )
    back_button.pack(pady=30)

    return client_list_screen_frame