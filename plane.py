from aircraft import Aircraft
import json


class Plane(Aircraft):
    def __init__(self, capacity, age, fuel_capacity):
        super().__init__(capacity, age, "PLANE", fuel_capacity)

    def add_to_record(self):
        with open("vehicle_records.json", "r+") as file:
            json_file = json.load(file)
            json_file["vehicle"]["plane"].append(self.dic)
            file.seek(0)
            json.dump(json_file, file, indent=4)
