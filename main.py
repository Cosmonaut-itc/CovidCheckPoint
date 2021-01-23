import requests

response = requests.get("http://api.name-fake.com/random/random.json")
nameID = response.json()['name']
print(nameID)
class Credential:
    def __init__(self, name, status, area, clearance):
        self.name = name
        self.status = status
        self.area = area
        self.clearance = clearance

class COVID:
    pass

class Person:
    pass


