from model import employeeStatus

dict1 = {}

def add(emp_no,info):
    dict1[emp_no] = info
    return dict1

def view():
    return dict1


def spec(emp_no):
    return dict1[emp_no]

def dept(no):
    a = []
    for i in dict1.values():
        if i.dept_id == no:
            a.append(i.name)
    return a

def present(p):
    if dict1.get(p) is not None:
        return employeeStatus(1,"got result",dict1[p])
    else:
        return employeeStatus(0,"no result",None)