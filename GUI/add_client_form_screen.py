import tkinter as tk
from typing import Callable
import client_form
import client as cl
import styles
from storage import temp_list



def render_add_client_form_screen_ui(
        container,
        return_add_client_screen: Callable[[], None]
) -> tk.Frame:
    # Отрисовка заглавного фрейма
    base_frame = tk.Frame(container, bg=styles.MAIN_BG_COLOR)

    base_frame.grid_columnconfigure(0, weight=1)
    base_frame.grid_rowconfigure(0, weight=1)

    # Отрисовка фрейма для формы ввода данных
    form_frame = tk.Frame(base_frame, bg=styles.MAIN_BG_COLOR)
    form_frame.grid(column=0, row=0, padx=20, pady=20)

    # Отрисовка формы для ввода данных
    form = client_form.ClientForm(form_frame)
    
    def save_data(form: Callable[[], None]) -> None:
        # Функция для извлечения данных клиента и переноса их в список
        data = form.get_data()
        client_data = cl.Client(**data)
        temp_list.append(client_data)

    # Отрисовка фрейма для кнопок
    button_frame = tk.Frame(base_frame, bg=styles.MAIN_BG_COLOR)
    button_frame.grid(column=0, row=1, pady=10)
    
    save_button = styles.make_style_button(
        button_frame,
        "Сохранить данные",
        styles.SILVER_BG_COLOR,
        styles.BLACK_TEXT_COLOR,
        command=lambda: save_data(form)
    )
    save_button.grid(column=0, row=0, padx=10, sticky="nsew")

    back_button = styles.make_style_button(
        button_frame,
        "Вернуться назад",
        styles.SILVER_BG_COLOR,
        styles.BLACK_TEXT_COLOR,
        command=return_add_client_screen
    )
    back_button.grid(column=1, row=0, padx=10, sticky="nsew")

    return base_frame


