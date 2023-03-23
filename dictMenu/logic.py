d = {}

def Add(word):
    if word in d.keys():
        d[word] = d[word] + 1
        return "Word already present, Count Added"
    else:
        d[word] = 1
        return "New Word Added"

def ViewWords():
    return d.keys()

def Occur():
    return d

def Spec(count):
    a = []
    for word in d:
        if d[word]>=count:
            a.append(word)
    return a




