list1 = [1,11,23,5,78,9,96,67,5]
list2 = [4,5,76,5,79,23,34,77,6,23,445]
x=[]

#return a list containing elements that are common without duplicates
for i in list1 :
    for y in list2:
        if i==y:
            x.append(i)

print(str(x))