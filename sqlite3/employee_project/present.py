from logic import viewEmp, insertEmp, viewDept

def init():
    exit = False
    # e1 = employee(1,"kishore",10,"chennai")
    # insertEmp(e1)
    # e2 = employee(2,"suresh",15,"delhi")
    # insertEmp(e2)
    # e3 = employee(3,"mohan",10,"vizag")
    # insertEmp(e3)
    while(exit == False):
        print("1.View employee by num\n2.View employee by deptID\n0.Exit")
        ch = int(input("Enter choice:"))

        if ch == 1:
            num = int(input("Enter employee num:"))
            message = viewEmp(num)
            if message.statuscode == 0:
                print("No employee Found")
            else:
                print("Employee Found",message.empobj)

        if ch == 2:
            deptid = int(input("Enter deptID:"))
            listOfEmployees = viewDept(deptid)
            if len(listOfEmployees) == 0:
                print("no employees found in the dept")
            else:
                for emp in listOfEmployees:
                    print(emp)


        elif ch == 0:
            exit = True