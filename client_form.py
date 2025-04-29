import tkinter as tk
import styles


class ClientForm:
    # Класс для отрисовки интерфейса и полей для записи данных клиента
    def __init__(self, container):
        self.entries = {}

        labels = ["Номер", "Имя", "Фамилия", "Номер телефона", "Описание"]

        for number, value in enumerate(labels):
            styles.make_style_label(
                container,
                value,
                styles.MAIN_BG_COLOR,
                styles.WHITE_TEXT_COLOR).grid(
                column=0, row=number, padx=5, pady=5)

            entry = styles.make_style_entry(container)
            entry.grid(column=1, row=number)

            self.entries[value] = entry

    def get_data(self):
        return {
            "client_id": self.entries["Номер"].get(),
            "name": self.entries["Имя"].get(),
            "surname": self.entries["Фамилия"].get(),
            "phone": self.entries["Номер телефона"].get(),
            "description": self.entries["Описание"].get(),
        }
