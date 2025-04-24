import tkinter as tk
from typing import Callable
import client_form
import client as cl
from storage import temp_list



def render_add_client_form_screen_ui(
        container,
        return_add_client_screen: Callable[[], None]
) -> tk.Frame:
    # Отрисовка заглавного фрейма
    base_frame = tk.Frame(container)

    base_frame.grid_columnconfigure(0, weight=1)
    base_frame.grid_rowconfigure(0, weight=1)

    # Отрисовка фрейма для формы ввода данных
    form_frame = tk.Frame(base_frame)
    form_frame.grid(column=0, row=0, padx=20, pady=20)

    form = client_form.ClientForm(form_frame)
    
    def save_data(form):
        data = form.get_data()
        client_data = cl.Client(**data)
        temp_list.append(client_data)

    # Отрисовка фрейма для кнопок
    button_frame = tk.Frame(base_frame)
    button_frame.grid(column=0, row=1, pady=10)
    
    save_button = tk.Button(
        button_frame,
        text="Сохранить",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=lambda: save_data(form)
    )
    save_button.grid(column=0, row=0, padx=10, sticky="nsew")

    back_button = tk.Button(
        button_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_add_client_screen
    )
    back_button.grid(column=1, row=0, padx=10, sticky="nsew")

    return base_frame


