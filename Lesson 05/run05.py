from typing import Any
users = {"Petro": "qwert", "Vovan": "asdfg"}
conversion_rate = {"usd": {"eur": 0.95, "chf": 0.89}, "eur": {"usd": 1.05, "chf": 0.93}, "chf": {"usd": 1.12, "eur": 1.07}}

class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def convert_currency(self, result_currency: str) -> "Price":
        if self.currency == result_currency:
            return self
        else:
            currency_rate  = conversion_rate[self.currency][result_currency]
            return Price(self.value * currency_rate, result_currency)

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Prices objects")
        else:
            if self.currency != other.currency:
                self_chf = self.convert_currency("chf")
                other_chf = other.convert_currency("chf")
                result_add = self_chf.value + other_chf.value
                result = Price(round(result_add), "chf").convert_currency(self.currency)
            else:
                result = Price(self.value + other.value, self.currency)
            return result

    def __sub__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Prices objects")
        else:
            if self.currency != other.currency:
                self_chf = self.convert_currency("chf")
                other_chf = other.convert_currency("chf")
                result_sub = self_chf.value - other_chf.value
                result = Price(round(result_sub), "chf").convert_currency(self.currency)
            else:
                result = Price(self.value - other.value, self.currency)
            return result

cached_data = {}
def auth(func):
    def wrapper():
        global cached_data
        if "username" in cached_data:
            return func()
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users.get(username) == password:
                cached_data = { "username": username, "password": password}
                print("Successful authorization")
                return func()
            else:
                print("Incorrect data. Please, try again")
    return wrapper

@auth
def command():
    print("Executing command")

phone = Price(value=200, currency="usd")
tablet = Price(value=400, currency="usd")
fridge = Price(value=700, currency="eur")
TV = Price(value=450,currency="eur")

total: Price = phone + tablet
print(total)
total_2: Price = fridge + tablet
print(total_2)
total_3: Price = TV - phone
print(total_3)
