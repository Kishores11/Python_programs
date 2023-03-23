class employee:
    def __init__(self,num,name,deptid,address):
        self.num = num
        self.name = name
        self.deptid = deptid
        self.address = address

    def __repr__(self):
        return f"{self.num},{self.name},{self.deptid},{self.address}"
    

class employeeStatus():
    def __init__(self,statuscode,message,empobj):
        self.statuscode = statuscode
        self.message = message
        self.empobj = empobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"
    