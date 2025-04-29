import tkinter as tk
from typing import Callable
import styles
from storage import temp_list



def render_client_list_screen_ui(
        container, 
        return_home_screen: Callable[[], None]
) -> tk.Frame:
    # Отрисовка заглавного фрейма
    base_frame = tk.Frame(container, bg=styles.MAIN_BG_COLOR)

    base_frame.grid_columnconfigure(0, weight=1)
    base_frame.grid_rowconfigure(0, weight=1)

    client_list_label = styles.make_style_label(
        base_frame,
        "В будущем здесь будет поиск",
        styles.MAIN_BG_COLOR,
        styles.FRAME_BG_COLOR,
        styles.TEXT_FONT
    )
    client_list_label.pack(expand=True)

    cards_frame = tk.Frame(base_frame, bg=styles.MAIN_BG_COLOR)
    cards_frame.pack(fill="both", expand=True, padx=20, pady=10)

    if not temp_list:
        no_clients_label = styles.make_style_label(
            cards_frame,
            "ЗДЕСЬ ПОКА НЕТ КЛИЕНТОВ!",
            styles.MAIN_BG_COLOR,
            styles.FRAME_BG_COLOR,
            styles.HEADER_FONT
        )
        no_clients_label.pack(expand=True)
    else:
        for client in temp_list:
            card = tk.LabelFrame(
                cards_frame,
                bd=0,
                bg=styles.FRAME_BG_COLOR,
                text=f"ID: {client.client_id}",
                font=styles.TEXT_FONT,
                padx=10,
                pady=10
            )
            card.pack(fill="x", padx=5, pady=5)

            full_name = f"{client.name} {client.surname}"
            info_label = styles.make_style_label(
                card,
                full_name,
                styles.FRAME_BG_COLOR,
                styles.BLACK_TEXT_COLOR
            )
            info_label.pack(anchor="w")

        # Кнопка на будущее
        details_button = styles.make_style_button(
            card,
            "Подробнее",
            styles.MAIN_BG_COLOR,
            styles.WHITE_TEXT_COLOR,
            None
        )
        details_button.pack(anchor="e", pady=5)

    back_button = styles.make_style_button(
        base_frame,
        "Вернуться назад",
        styles.FRAME_BG_COLOR,
        styles.BLACK_TEXT_COLOR,
        command=return_home_screen
    )
    back_button.pack(pady=30)

    return base_frame