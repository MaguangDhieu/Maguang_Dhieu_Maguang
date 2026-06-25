class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def price(self):
        return self.__price

car1 = Car("Toyota", "MC2019", 2000)
print(car1.brand)
print(car1._model)
print(car1.price)


       
               