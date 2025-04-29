import tkinter as tk
from typing import Callable
import styles


def render_home_screen_ui(
        container,
        show_add_client_screen: Callable[[], None],
        show_client_list_screen: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса домашнего экрана
    # Создание заглавного фрейма
    home_frame = tk.Frame(container, bg=styles.MAIN_BG_COLOR)

    home_frame.grid_columnconfigure(0, weight=1)
    home_frame.grid_rowconfigure(0, weight=1)

    # Создание фрейма, который будет вставлен в home_frame
    client_controls_frame = tk.LabelFrame(
        home_frame,
        bd=0,
        text="Управление клиентами",
        bg=styles.FRAME_BG_COLOR,
        labelanchor="n",
        padx=30,
        pady=30,
        font=("Arial", 10, "bold")
    )
    client_controls_frame.pack(expand=True, pady=30)

    # Создание и отрисовка кнопки добавления клиента
    adding_button = styles.make_style_button(
        client_controls_frame,
        "Добавить клиента",
        styles.MAIN_BG_COLOR,
        styles.WHITE_TEXT_COLOR,
        show_add_client_screen
    )
    adding_button.pack(pady=15)

    # Создание и отрисовка кнопки, открывающей список клиентов
    user_list_button = styles.make_style_button(
        client_controls_frame,
        "Список действующих клиентов",
        styles.MAIN_BG_COLOR,
        styles.WHITE_TEXT_COLOR,
        show_client_list_screen
    )
    user_list_button.pack(pady=15)

    return home_frame
