class Aircraft:
    def __init__(self, capacity, age, type_aircraft, fuel_capacity):
        self.type = type_aircraft
        self.capacity = capacity
        self.age = age
        self.id = "testID"
        self.fuel = fuel_capacity
        self.dic = {"capacity": f"{self.capacity}",
                    "age": f"{self.age}",
                    "fuel": f"{self.fuel}",
                    "id": f"{self.id}",
                    "colour": "salmon pink"
                    }

    def fly_between(self, city1, city2):
        pass
