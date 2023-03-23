class Employee:

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def call(self):
        print(self.name,self.address)

e1 = Employee("kishore","karur")
e2 = Employee("Mahesh","Erode")

e1.call()
e2.call()