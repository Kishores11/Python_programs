import json
from json import JSONEncoder
class Task:
    def __init__(self,name,desc,priority):
        self.name = name
        self.desc = desc
        self.priority = priority


    def __repr__(self):
        return f"Name: {self.name},Descrption: {self.desc},Priority: {self.priority}"
    
class EmployeeEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__