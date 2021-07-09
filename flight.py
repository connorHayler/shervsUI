import json
from helicopter import Helicopter
from plane import Plane


class Flight:
    def __init__(self, flight_id, destination, origin, vehicle, duration):
        self.flight_id = flight_id
        self.destination = destination
        self.origin = origin
        self.vehicle = vehicle
        self.duration = duration
        self.seats_remaining = vehicle.capacity
        self.add_records()
        self.passenger = []

    def add_records(self):
        new_flight = {'id': self.flight_id,
                      'destination': self.destination,
                      'origin': self.origin,
                      'vehicle': self.vehicle.dic,
                      "seats_remaining": self.seats_remaining,
                      'duration': self.duration,
                      'passenger': []
                      }

        # Reads, Updates and Closes json file
        try:
            with open("flight_records.json", "r+") as read_file:
                data = json.load(read_file)
                data["flight"].append(new_flight)
                read_file.seek(0)
                json.dump(data, read_file, indent=4)
        except FileNotFoundError as err:
            return "File not found"

    def add_passenger(self, passenger):
        with open("flight_records.json", "r+") as file:
            data = json.load(file)
            for index, flight in enumerate(data["flight"]):
                if flight["id"] == self.flight_id:
                    break
            if data["flight"][index]["seats_remaining"] > 0:
                if passenger.age >= 2:
                    data["flight"][index]["seats_remaining"] -= 1
                data["flight"][index]["passenger"].append(passenger.dic)
                file.seek(0)
                json.dump(data, file, indent=4)
                self.passenger.append(passenger)
            else:
                return False

    def report(self):
        return report_string(self.flight_id)

    # def generate_flight_attendees(self):
    #     try:
    #         identity = open("passengers.json", "r")
    #         id = json.load(identity)
    #         for value, key in id.items():
    #             if not isinstance(key, list):
    #                 for x, y in key.items():
    #                     print(x, ':', y)
    #             else:
    #                 for i in key:
    #                     for s, m in i.items():
    #                         print(s, ':', m)
    #     except FileNotFoundError as err:
    #         return "File not found"

    # Function to change flight trip details
    def manage_flight_trips(self, destination, origin, vehicle, duration):
        # Open json file as read only to get a dict
        self.destination = destination
        self.origin = origin
        self.vehicle = vehicle
        self.duration = duration
        try:
            with open("flight_records.json", "r+") as file:
                json_file = json.load(file)
                flights_json = json_file["flight"]

                # Iterate through dict to see if flight id is the same as what was inputted
                for index, flight in enumerate(flights_json):
                    # If there's a flight with the same id, change the details
                    if flight["id"] == self.flight_id:
                        break
                json_file["flight"][index]["destination"] = self.destination
                json_file["flight"][index]["origin"] = self.origin
                json_file["flight"][index]["vehicle"] = self.vehicle.dic
                json_file["flight"][index]["duration"] = self.duration
                # # Iterate through the passengers of the flight
                # for passenger in flight["passenger"]:
                #     # If there's a passenger with the same id, change details
                #     if passenger["passport"] == passenger_id:
                #         passenger["seat"] = seat
                file.seek(0)
                json.dump(json_file, file, indent=4)
        except FileNotFoundError as err:
            return "File not found"

    # User input
    # create_flight("JH255", "Portugal", "England", "Plane", "200")
    # manage_flight_trips("W1", "Greece", "USA", "Helicopter", "120")
    # print(generate_flight_attendees())


def report_string(flight_id=None):
    report_list = []
    if flight_id is None:
        return "Sorry there is no flights for this flight ID"
    else:
        with open("flight_records.json") as file:
            json_file = json.load(file)
            for index, flight in enumerate(json_file["flight"]):
                if flight["id"] == flight_id:
                    break
            for passenger in json_file["flight"][index]["passenger"]:
                fname = passenger["fName"]
                lname = passenger["lName"]
                passport = passenger["passport"]
                report_list.append((fname, lname, passport))
        return report_list


def find_vehicle(vehicle_ID):
    with open("vehicle_records.json") as file:
        json_file = json.load(file)
        for plane in json_file["vehicle"]["plane"]:
            if plane["id"] == vehicle_ID:
                plane_return = Plane(plane["capacity"], plane["age"], plane["fuel"])
                return plane_return
        for helicopter in json_file["vehicle"]["helicopter"]:
            if helicopter["id"] == vehicle_ID:
                helicopter_return = Helicopter(helicopter["capacity"], helicopter["age"], helicopter["fuel"])
                return helicopter_return
        return None