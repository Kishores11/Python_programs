def area(a,b,c):
    s = (a+b+c)/2
    result =  (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return result

def start():
    x = int(input("Enter side 1:"))
    y = int(input("Enter side 2:"))
    z = int(input("Enter side 3:"))
    message = area(x,y,z)
    print('%0.2f' %message)

start()