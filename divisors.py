#Ask user for number
num = int(input("Give me a number: "))
#create a list and specify a range
listRange= list(range(1,num+1))
#empty array to add divisor to
divisors=[]
#loop through num given range 
for number in listRange:
    if num % number == 0:
        divisors.append(number)
#prints all divisors for the number

print(divisors)