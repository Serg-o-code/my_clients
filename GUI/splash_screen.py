import tkinter as tk
from typing import Callable


def show_splash_screen(
    launch_main_app: Callable,
    text: str = "Добро пожаловать",
    name: str = "пользователь"
) -> None:
    # Функция для создания заставки
    splash = tk.Tk()
    splash.overrideredirect(True)  # Убрать рамки окна
    splash.geometry("400x250+600+250")  # Размер окна + расположение на экране

    splash.configure(bg="#1e1e1e")  # Фоновый цвет

    label = tk.Label(splash, text=f"{text}, {name}!", font=(
        "Arial", 14), bg="#1e1e1e", fg="white")  # Настройка приветствия
    label.pack(expand=True)  # Размещение посередине экрана

    # После окончания заставки будет запущен основной цикл
    try:
        splash.after(2500, lambda: launch_main_app(splash))
        splash.mainloop()
    except Exception as e:
        print(f"Ошибка запуска главного окна: {e}")
