listA = ["hg12","65","hge692jhde"]

#Given dlist
print("Given list: ",listA)
# Add the numeric values
res = sum(filter(lambda i: isinstance(i, int), listA))
print ("Sum of numbers in listA: ", res)