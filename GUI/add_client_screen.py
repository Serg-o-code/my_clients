import tkinter as tk
from typing import Callable


def render_add_client_screen_ui(
        container,
        add_client_form_screen: Callable[[], None], 
        return_home_screen: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса экрана добавления клиента
    base_frame = tk.Frame(container)  # Создание базового фрейма

    add_client_form_frame = tk.LabelFrame(
        base_frame,
        text="Добавление нового клиента",
        labelanchor="n",
        padx=30,
        pady=30,
        font=("Arial", 10, "bold")
    )
    add_client_form_frame.pack(pady=60)

    adding_button = tk.Button(
        add_client_form_frame,
        text="Добавить нового клиента",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=add_client_form_screen
    )
    adding_button.grid(column=0, row=0, padx=15, pady=15)

    return_button = tk.Button(
        add_client_form_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_home_screen
    )
    return_button.grid(column=0, row=1, padx=15, pady=15)

    return base_frame
