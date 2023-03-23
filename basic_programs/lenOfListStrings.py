def lenOfListStrings(x):
    result = []
    for i in x:
        result.append(len(i)) 
    return result

def start():
    list1 = ["how are you","hi","hello kishore"]
    message = lenOfListStrings(list1)
    print(message)


start()