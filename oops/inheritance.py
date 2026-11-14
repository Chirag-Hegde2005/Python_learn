class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.brand} {self.model}'s engine is starting...")

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def charge(self):
        print(f"Charging the {self.battery_size} kWh battery of the {self.model}.")

    def start_engine(self):
        print(f"The {self.brand} {self.model} powers on silently!")

class SportsCar(Car):
    def __init__(self, brand, model, year, top_speed):
        super().__init__(brand, model, year)
        self.top_speed = top_speed

    def activate_turbo(self):
        print(f"{self.brand} {self.model} turbo engaged! Top speed: {self.top_speed} km/h.")

my_ev = ElectricCar("Tesla", "Model 3", 2025, 75)
my_ev.display_info()
my_ev.start_engine()
my_ev.charge()

print("-" * 40)

my_sports = SportsCar("Porsche", "911", 2024, 310)
my_sports.display_info()
my_sports.start_engine()
my_sports.activate_turbo()