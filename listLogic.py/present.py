from logic import randomList, view, change, removeelem, asc, des, Occurance, backUp, restore


def fillList():
    randomList()
    print("Filled 10 random nos")
    print("\n")


def viewList():
    message = view()
    print(message)
    print("\n")


def changeNum():

    a = int(input("Enter the no:"))
    b = int(input("Enter the new no:"))
    message = change(a,b)
    print(message)
    print("\n")

        
def remove():
    ele = int(input("Enter the num to remove:"))
    message = removeelem(ele)
    print(message)
    print("\n")


def sortasc():
    message = asc()
    print(message)

def sortdes():
    message = des()
    print(message)


def init():

    exit = False

    while exit == False:
        print("1.Fill up list with 10 random nos")
        print("2.View all the list")
        print("3.Change the no")
        print("4.Remove element")
        print("5.Sort in ascending")
        print("6.Sort in descending")
        print("7.Occurance of nums")
        print("8.Back up")
        print("9.Restore")
        print("0.exit")

        ch = int(input("Enter choice:"))
        if ch == 1:
            fillList()
    

        elif ch == 2:
            viewList()

        elif ch == 3:
            changeNum()

        elif ch == 4:
            remove()

        elif ch == 5:
            sortasc()

        elif ch == 6:
            sortdes()

        elif ch == 7:
            message = Occurance()
            print(message)

        elif ch == 8:
             backUp()
             print("Converted into JSON format")

        elif ch == 9:
            restore()
            print("File restored")


        elif ch == 0:
            exit = True
            print("-------------------")





