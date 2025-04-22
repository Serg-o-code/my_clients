import tkinter as tk
from typing import Callable


def render_home_screen_ui(
        container,
        add_client_func: Callable[[], None],
        show_client_list: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса домашнего экрана
    home_frame = tk.Frame(container)  # Создание заглавного фрейма

    # Создание фрейма, который будет вставлен в main_frame
    client_controls_frame = tk.LabelFrame(
        home_frame,
        text="Управление клиентами",
        labelanchor="n",
        padx=30,
        pady=30,
        font=("Arial", 10, "bold")
    )
    client_controls_frame.pack(pady=60)

    # Создание и отрисовка кнопки добавления клиента
    adding_button = tk.Button(
        client_controls_frame,
        text="Добавить клиента",
        padx=25,
        pady=25,
        borderwidth=15,
        font=("Calibri", 12, "bold"),
        command=add_client_func
    )
    adding_button.grid(column=0, row=0, padx=15, pady=15)

    # Создание и отрисовка кнопки, открывающей список клиентов
    user_list_button = tk.Button(
        client_controls_frame,
        text="Список клиентов",
        padx=25,
        pady=25,
        borderwidth=15,
        font=("Calibri", 12, "bold"),
        command=show_client_list
    )
    user_list_button.grid(column=0, row=1, padx=15, pady=15)

    return home_frame
