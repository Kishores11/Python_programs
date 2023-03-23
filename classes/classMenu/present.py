from logic import addTask, present, viewTask, updateTask, removeTask, viewAll, backUp, restore
from model import Task

def start():
    exit = False
    while(exit == False):
        print("\n1.Task operation\n2.View all tasks\n3.Back up\n4.Restore\n0.Exit")
        ch = int(input("Enter choice:"))
        
        if ch == 1:
            id = int(input("Enter task id:"))
            task(id)

        elif ch == 2:
            message = viewAll()
            print(message)

        elif ch == 3:
            backUp()
            print("Converted into json file")

        elif ch == 4:
            restore()
            print("Content restored")


        elif ch == 0:
            exit = True


def task(id):
    t1 = present(id)
    if t1 == 1:
        exit = False
        print("Task found")
        while(exit == False):
                print("\n1.Update task info\n2.View task info\n3.Remove task info\n0.exit")
                ch = int(input("Enter choice:"))

                if ch == 1:
                    b = input("Enter new task name:")
                    c = input("Enter new task desc:")
                    d = input("Enter new task priority:")
                    task = Task(b,c,d)
                    message = updateTask(id,task)
                    print(message)

                elif ch == 2:
                    message = viewTask(id)
                    print(message)

                elif ch == 3:
                    message = removeTask(id)
                    print(message)


                elif ch == 0:
                    exit = True
        
    else:
        print(t1)
        print("---create task-----")
        b = input("Enter task name:")
        c = input("Enter task desc:")
        d = int(input("Enter task priority:"))
        t1 = Task(b,c,d)
        message = addTask(id,t1)
        print(message)