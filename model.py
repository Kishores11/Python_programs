class employee:
    def __init__(self, id, name, dept_id, address):
        self.id = id
        self.name = name
        self.dept_id = dept_id
        self.address = address

    def __repr__(self):
        return f"id:{self.id},name:{self.name},dept_id:{self.dept_id},address:{self.address}"


class employeeStatus():
    def __init__(self, statuscode, message, empobj):
        self.statuscode = statuscode
        self.message = message
        self.empobj = empobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"
