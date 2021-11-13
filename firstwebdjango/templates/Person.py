import json


class Person:
    def __init__(self, firstName, lastName):
        self.FirstName = firstName
        self.LastName = lastName

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)