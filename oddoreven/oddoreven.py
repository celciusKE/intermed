num = int(input("Give me a number: "))
check = int(input("Give me number to divide by: "))
mod = num%2

if mod>0:
    print("Thats even")
else:
    print("Thats odd")

if num%check==0:
    print("this number divides evenly into "+str(num))
else:
    print("this number is not divisible "+str(num))