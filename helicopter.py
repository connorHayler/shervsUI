from aircraft import Aircraft
import json


class Helicopter(Aircraft):
    def __init__(self, capacity, age, fuel_capacity):
        super().__init__(capacity, age, "HELICOPTER", fuel_capacity)

    def add_to_record(self):
        dic = {"capacity": f"{self.capacity}",
               "age": f"{self.age}",
               "fuel": f"{self.fuel}",
               "id": f"{self.id}"
               }
        with open("vehicle_records.json", "r+") as file:
            json_file = json.load(file)
            json_file["vehicle"]["helicopter"].append(dic)
            file.seek(0)
            json.dump(json_file, file, indent=4)
