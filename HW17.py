from datetime import date

class Car:
 number_of_cars = 0

 def  __init__(self, brand, model, year):
   self.__brand = brand
   self.__model = model
   self.__year = year
   Car.number_of_cars +=1

 def car_info(self):
  print(f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__year}")

 def age_of_car(self):
        current_year = date.today().year
        age = current_year - int(self.__year)
        return age
 
 @classmethod
 def total_cars(cls):
   return cls.number_of_cars

class Electric_car (Car):
 def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.__battery_life = battery_life

 def battery_inf(self):
       print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.__battery_life} საათი")

car1 = Car("Toyota", "Camry", "2020")
car1.car_info()
car1.age_of_car()

print(f"Age of the car: {car1.age_of_car()} years")
print(f"Total number of cars: {Car.total_cars()}")
electric_car1 = Electric_car("Tesla", "ModelS", "2022", "100")
print(f"Age of the electric car: {electric_car1.age_of_car()} years")
electric_car1.car_info()
electric_car1.battery_inf()
print(f"Total number of cars: {Car.total_cars()}")
