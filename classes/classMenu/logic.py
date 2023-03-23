import json
from model import EmployeeEncoder

dict1 = {}


def present(id):
    if dict1.get(id) is not None:
        return 1
    else:
        return "No such id"
    

def addTask(id,t1):
    dict1[id] = t1
    return "Task Added"


def viewTask(id):
    return dict1[id]


def updateTask(id,newtask):
    dict1[id] = newtask
    return "Task Updated"


def removeTask(id):
    del dict1[id]
    return "Task Deleted"


def viewAll():
    return dict1

def backUp():
    enc = EmployeeEncoder().encode(dict1)
    with open('task.txt','w') as f:
        f.write(enc)

def restore():
    with open('task.txt','r') as f:
        data = json.loads(f.read())
        for key, value in data.items():
            dict1[key] = value   
             