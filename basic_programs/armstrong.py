num = int(input('Enter no:'))
num2 = num
num3 = num
s = 0
count = 0

while num != 0:
    count = count + 1
    num = num//10


while num2 != 0:
    r = num2 % 10
    s = s + (r**count)
    num2 = num2//10

if num3 == s:
    print('It is armstrong no')

else:
    print('It is not an armstrong no')

