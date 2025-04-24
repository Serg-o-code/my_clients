import tkinter as tk
from typing import Callable
from storage import temp_list


def render_client_list_screen_ui(
        container, 
        return_home_screen: Callable[[], None]
) -> tk.Frame:
    # Отрисовка заглавного фрейма
    base_frame = tk.Frame(container)

    base_frame.grid_columnconfigure(0, weight=1)
    base_frame.grid_rowconfigure(0, weight=1)

    client_list_label = tk.Label(
        base_frame,
        text="Список клиентов",
        padx=10,
        pady=10,
        font=("Arial", 14, "bold")
    )
    client_list_label.pack(expand=True)

    cards_frame = tk.Frame(base_frame)
    cards_frame.pack(fill="both", expand=True, padx=20, pady=10)

    if not temp_list:
        no_clients_label = tk.Label(
        cards_frame,
        text="Здесь пока нет клиентов!",
        padx=10,
        pady=10,
        font=("Arial", 20, "bold")
    )
        no_clients_label.pack(expand=True)
    else:
        for client in temp_list:
            card = tk.LabelFrame(
                cards_frame,
                text=f"ID: {client.client_id}",
                font=("Arial", 10, "bold"),
                padx=10,
                pady=10
            )
            card.pack(fill="x", padx=5, pady=5)

        full_name = f"{client.name} {client.surname}"
        info_label = tk.Label(card, text=full_name, font=("Calibri", 12))
        info_label.pack(anchor="w")

            # Кнопка на будущее
        details_button = tk.Button(
            card,
            text="Подробнее",
            font=("Calibri", 10),
            padx=5,
            pady=2
        )
        details_button.pack(anchor="e", pady=5)

    back_button = tk.Button(
        base_frame,
        text="Назад",
        padx=25,
        pady=25,
        font=("Calibri", 16, "bold"),
        command=return_home_screen
    )
    back_button.pack(pady=30)

    return base_frame