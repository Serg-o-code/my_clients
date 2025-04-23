class Client:
    # Класс для сбора данных о клиенте
    def __init__(self, client_id, name, surname, phone, description):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.description = description
