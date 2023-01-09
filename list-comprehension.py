a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
ages = []

#make a new list that has only even numbers
for n in a:
    if n%2 == 0:
        ages.append(n)
print(ages)

ages = [n for n in a if n%2 == 0]
print(ages)