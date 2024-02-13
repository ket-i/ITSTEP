class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Brand must be a text")
        else:
            self._brand = brand

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Model must be a text")
        else:
            self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        else:
            self._year = year

    def get_year(self):
        return self._year


# Example usage:
car = Car("Hyundai", "Tucson", 2017)

print("Brand:", car.get_brand())
print("Model:", car.get_model())
print("Year:", car.get_year())