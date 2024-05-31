import json



try:

    class Paynet:
        def __init__(self, first_name: str, last_name: str, phone: str, card: str, card_period, balance: int):
            self.first_name = first_name
            self.last_name = last_name
            self.card = card
            self.phone = phone
            self.card_period = card_period
            self.balance = balance



        def save(self):
            with open("database.json", encoding="utf-8") as file:
                data = json.load(file)
            with open("database.json", "w") as f:
                new = {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "card": self.card,
                    "phone": self.phone,
                    "card_period": self.card_period
                }
                data["users"].append(new)
                json.dump(data, f, indent=6)

    class Card(Paynet):
        def __init__(self, first_name, last_name, card, card_period, phone, balance: int, date):
            Paynet.__init__(self, first_name, last_name, card, card_period, phone, balance)
            self.date = date

        def __str__(self):
            return f""" Ism: {self.first_name} 
                        Familiya: {self.last_name}
                        Karta: {self.card}
                        Balans: {self.balance}"""

        def get_balance(self):
            return f"{self.balance}"

        def get_phone(self):
            return f"{self.phone}"

except Exception as error:
    print(f"{error}")