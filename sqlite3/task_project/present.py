from logic import addTask, present, updateTask, viewTask, removeTask
from model import Task

def init():
    exit = False
    while(exit == False):
        print("\n1.Task operation\n0.Exit")
        ch = int(input("Enter choice:"))
        
        if ch == 1:
            id = int(input("Enter task id:"))
            task(id)

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
                    task = Task(id,b,c,d)
                    message = updateTask(task)
                    if message == 1:
                        print("Task updated Successfully")
                    else:
                        print("Failed")
                         

                elif ch == 2:
                    message = viewTask(id)
                    print("task Name:",message.name)
                    print("task Description:",message.desc)
                    print("task Priority:",message.priority)


                elif ch == 3:
                    msg = removeTask(id)
                    if msg == 1:
                        print("Task Deleted")


                elif ch == 0:
                    exit = True
        
    else:
        print("---No such Task, Create one----")
        a = int(input("Enter task id:"))
        b = input("Enter task name:")
        c = input("Enter task desc:")
        d = int(input("Enter task priority:"))
        t1 = Task(a,b,c,d)
        msg = addTask(t1)
        if message == 1:
            print("Task Added Successfully")
        else:
            print("Failed")