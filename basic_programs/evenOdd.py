def func(a):
    odd = []
    even = []
    for i in a:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (odd,even)


arr = [1,2,3,4,5,6]
message = func(arr)
print(message)