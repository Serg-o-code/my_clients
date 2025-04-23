import tkinter as tk
from typing import Callable
import client_form

def render_add_client_form_screen_ui(
        container, 
        return_add_client_screen: Callable[[], None]
) -> tk.Frame:
    # Метод для отрисовки интерфейса экрана списка клиентов
    base_frame = tk.Frame(container)

    form_frame = tk.Frame(base_frame)
    form_frame.pack()

    add_client_form_screen_frame = tk.Frame(form_frame)
    client_form.ClientForm(add_client_form_screen_frame)
    add_client_form_screen_frame.pack(expand=True)

    back_button = tk.Button(
        base_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_add_client_screen
    )
    back_button.pack(pady=30)

    return base_frame
    # client_list_label = tk.Label(
    #     client_list_screen_frame,
    #     text="Список клиентов",
    #     padx=10,
    #     pady=10,
    #     font=("Arial", 14, "bold")
    # )
    # client_list_label.pack(expand=True)



    # return client_list_screen_frame