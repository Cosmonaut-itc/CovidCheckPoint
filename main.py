import requests

response = requests.get("http://api.name-fake.com/random/random.json")
name = response.json()



class Credential:
    def __init__(self, name, status, area, clearance):
        self.name = name
        self.status = status
        self.area = area
        self.clearance = clearance

class COVID:
    def __init__(self, date, actual_date,  dice, days, validity):
        self.date = date
        self.actual_date = actual_date
        self.dice = dice
        self.days = days
        self.validity = validity

class Mask: 
    def __init__(self, wearsMask):
        self.wearsMask = wearsMask


