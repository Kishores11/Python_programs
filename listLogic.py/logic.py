import random, json

randomlist = [] 

def randomList():
    for i in range(0,10):
        n = random.randint(0,100)
        randomlist.append(n)

def view():
    return randomlist

def change(a,b):
    if a not in randomlist:
        return "Num not in list"
    elif b in randomlist:
        return "Num already in list"
    
    else:
        i = randomlist.index(a)
        randomlist[i] = b
        return "Num changed"
         

def removeelem(ele):
    if ele in randomlist:
        randomlist.remove(ele)
        return "Num removed"
    else:
        return "No such num"
    
def asc():
    asc = randomlist.copy()
    asc.sort()

    return asc

def des():
    des = randomlist.copy()
    des.sort(reverse=True)
    return des

def Occurance():
    a = []
    b = []
    counter = 0
    for i in randomlist:
        frequency = randomlist.count(i)
        counter = frequency
        a.append(i)
        b.append(counter)
    return dict(zip(a,b))
        
def backUp():
    jsonObj = json.dumps(randomlist)
    with open('sample.txt','w') as outfile:
        outfile.write(jsonObj)

def restore():
    with open('sample.txt','r') as outfile:
        py = json.loads(outfile.read())
        for i in py:
            randomlist.append(i)


    