import os
from tkinter import Tk


class MainApp:
    # Класс для управления ресурсами и поведением приложения
    def __init__(self, root):
        self.root = root
        self.root.title("My clients")
        
        # Установка иконки приложения
        icon_path = os.path.join(os.path.dirname(
            __file__), "resources", "icon.ico")
        self.root.iconbitmap(icon_path)



if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
