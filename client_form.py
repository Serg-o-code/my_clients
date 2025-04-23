import tkinter as tk


class ClientForm:
    # Класс для отрисовки интерфейса и полей для записи данных клиента
    def __init__(self, container):
        self.entries = {}

        labels = ["Номер", "Имя", "Фамилия", "Номер телефона", "Описание"]

        for number, value in enumerate(labels):
            tk.Label(container, text=value, padx=5, pady=5).grid(
                column=0, row=number, padx=5, pady=5)
            
            entry = tk.Entry(container, width=40)
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
