from logic import add, view, spec, dept, present
from model import employee

def init():
    exit = False
    e1 = employee("kishore",10,"chennai")
    add(1,e1)
    e2 = employee("suresh",10,"delhi")
    add(2,e2)
    e3 = employee("mohan",10,"vizag")
    add(3,e3)
    while(exit == False):
        print("1.View all\n2.View specific\n3.By department\n4.status check\n0.Exit")
        ch = int(input("Enter choice:"))
        
        if ch == 1:
            message = view()
            print(message)

        elif ch == 2:
            no = int(input("Enter emp_no:"))
            message = spec(no)
            print(message)

        elif ch == 3:
            no = int(input("Enter dept_id:"))
            message = dept(no)
            print(message)

        elif ch == 4:
            no = int(input("Enter employee no:"))
            p = present(no)
            print(p)
 

        elif ch == 0:
            exit = True

        