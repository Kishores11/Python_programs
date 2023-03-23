from db import getEmployeeInfo, insertemployee, getDeptInfo


def insertEmp(info):
    insertemployee(info)

def viewEmp(num):
    emp = getEmployeeInfo(num)
    return emp

def viewDept(num):
    dept = getDeptInfo(num)
    return dept
    