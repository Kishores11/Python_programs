from model import employee

e1 = employee("kishore",10,"chennai")

dict1 = {e1.name: e1}

var = dict1.get(e1.name)

print(var)