class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print(self.name,self.age)



p1 = Person("John", 36)
p2 = Person("kishore",22)

p1.fun()
p2.fun()
