def addNum(x,y):
    result = x+y
    return result

def start():
    x = int(input("Enter num1:"))
    y = int(input("Enter num2:"))
    message = addNum(x,y)
    print(message)

start()