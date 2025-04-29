import tkinter as tk
from typing import Callable
import styles


def render_add_client_screen_ui(
        container,
        show_add_client_form_screen: Callable[[], None],
        return_home_screen: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса экрана добавления клиента
    # Создание базового фрейма
    base_frame = tk.Frame(container, bg=styles.MAIN_BG_COLOR)

    base_frame.grid_columnconfigure(0, weight=1)
    base_frame.grid_rowconfigure(0, weight=1)

    add_client_form_frame = tk.LabelFrame(
        base_frame,
        bd=0,
        text="Добавление нового клиента",
        bg=styles.FRAME_BG_COLOR,
        labelanchor="n",
        padx=30,
        pady=30,
        font=("Arial", 10, "bold")
    )
    add_client_form_frame.pack(expand=True, pady=30)

    adding_button = styles.make_style_button(
        add_client_form_frame,
        "Добавить нового клиента",
        styles.MAIN_BG_COLOR,
        styles.WHITE_TEXT_COLOR,
        show_add_client_form_screen
    )
    adding_button.pack(pady=15)

    return_button = styles.make_style_button(
        add_client_form_frame,
        "Вернуться назад",
        styles.MAIN_BG_COLOR,
        styles.WHITE_TEXT_COLOR,
        return_home_screen
    )
    return_button.pack(pady=15)

    return base_frame
