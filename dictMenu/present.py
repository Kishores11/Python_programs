from logic import Add, ViewWords, Occur, Spec

def start():
    exit = False
    while(exit == False):
        print("\n1.Add a word \n2.View all words \n3.Occuring of all word \n4.Enter specific count"
              "\n0.Exit")
        ch = int(input("Enter your choice:"))

        if ch == 1:
            word = input("Enter word to add:")
            message = Add(word)
            print(message)

        elif ch == 2:
            message = ViewWords()
            print(message)

        elif ch == 3:
            message = Occur()
            print(message)

        elif ch == 4:
            count = int(input("Enter the count:"))
            message = Spec(count)
            print(message)

        elif ch == 0:
            exit = True
            print("-----------------")
