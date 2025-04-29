import tkinter as tk


# Цветовая палитра
MAIN_BG_COLOR = "#002366"
SECONDARY_BG_COLOR = "#005f99"
FRAME_BG_COLOR = "#ead2a8"
SILVER_BG_COLOR = "#e0e0e0"
ENTRY_BG_COLOR = "#ffffff"
BLACK_TEXT_COLOR = "#000000"
WHITE_TEXT_COLOR = "#ffffff"

# Шрифты
HEADER_FONT = ("Arial", 20, "bold")
TEXT_FONT = ("Arial", 14)
BUTTON_FONT = ("Calibri", 14, "bold")

# Стиль кнопок
def make_style_button(master, text, bg, fg, command=None):
    return tk.Button(
        master,
        text=text,
        bg=bg,
        fg=fg,
        activebackground=SECONDARY_BG_COLOR,
        activeforeground="white",
        font=BUTTON_FONT,
        relief="flat",
        borderwidth=0,
        padx=15,
        pady=10,
        command=command
    )

# Стиль Entry
def make_style_entry(master):
    entry = tk.Entry(
        master,
        bg=ENTRY_BG_COLOR,
        fg=MAIN_BG_COLOR,
        font=TEXT_FONT,
        relief="flat",
        width=40
    )
    entry.config(highlightbackground=MAIN_BG_COLOR, highlightthickness=1)
    return entry

# Стиль Label
def make_style_label(master, text, bg, fg, font=TEXT_FONT):
    return tk.Label(
        master,
        text=text,
        bg=bg,
        fg=fg,
        font=font
    )
