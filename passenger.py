import json


# Creates a passenger and adds passenger info to database
class Passenger:
    def __init__(self, first_name, last_name, passport_number, age):
        self.f_name = first_name
        self.l_name = last_name
        self.passport = passport_number
        self.age = age
        self.dic = {'passport': self.passport,
                    'fName': self.f_name.lower(),
                    'lName': self.l_name.lower(),
                    'age': self.age}

    def add_record(self):
        # Some function to not reduce seat number

        # Reads, Updates and Closes json file
        with open("passenger_records.json", "r+") as file:
            data = json.load(file)
            data["passenger"].append(self.dic)
            file.seek(0)
            json.dump(data, file, indent=4)


def get_passenger():
    report_list = []
    with open("passenger_records.json", "r") as file:
        json_file = json.load(file)
        for passenger in json_file["passenger"]:
            fname = passenger["fName"]
            lname = passenger["lName"]
            passport = passenger["passport"]
            age = passenger["age"]
            report_list.append((fname, lname, passport, age))
    return report_list

