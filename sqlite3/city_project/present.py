from model import city
from logic import addCity, changeCity, changeArea, viewCity, pincode, sortCity, sortArea, sortPin


def init():
    exit = False
    while exit == False:
        print("\n1.Add city information\n2.Change city information\n3.View city information"
              "\n4.Find By pincode\n5.Sort\n0.Exit\n")
        
        ch = int(input("Enter your choice:"))

        if ch == 1:
            a = input("Enter city name:")
            b = input("Enter area name:")
            c = int(input("Enter pincode:"))
            info = city(a,b,c)
            msg = addCity(info)
            if msg == 1:
                print("Added Successfully")
            else:
                print("Not Added")

        elif ch == 2:
            print("\n1.Change city name\n2.Change area name")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                a = input("Enter old city name:")
                b = input("Enter new city name:")
                msg = changeCity(a,b)
                if msg == 1:
                    print("City Name Updated")
                else:
                    print("No such city name")

            elif ch == 2:
                a = input("Enter old area name:")
                b = input("Enter new area name:")
                msg = changeArea(a,b)
                if msg == 1:
                    print("Area Name Updated")
                else:
                    print("No such area name")

        elif ch == 3:
            a = input("Enter city name:")
            msg = viewCity(a)
            if len(msg) == 0:
                print("No such City")
            else:
                print(msg)

        elif ch == 4:
            a = input("Enter pincode:")
            msg = pincode(a)
            if msg.statuscode == 0:
                print("No such Pincode")
            else:
                print("City Found",msg.cityobj)

        elif ch == 5:
            print("\n1.Sort by cityname\n2.Sort by areaname\n3.Sort by pincode")
            ch = int(input("Enter your choice:"))

            if ch == 1:
                msg = sortCity()
                if len(msg) != 1:
                    print("Sorted")
                    print(msg)
                else:
                    print("Not Sorted")
            elif ch == 2:
                msg = sortArea()
                if len(msg) != 1:
                    print("Sorted")
                    print(msg)
                else:
                    print("Not Sorted")
            elif ch == 3:
                msg = sortPin()
                if len(msg) != 1:
                    print("Sorted")
                    print(msg)
                else:
                    print("Not Sorted")



        elif ch == 0:
            exit = True

