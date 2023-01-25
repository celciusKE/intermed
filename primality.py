#ask user for number
num = int(input("Give me a prime number: "))
#determine if number is prime

#if x in x,in range of 2 and num , divides by num =0
a=[x for x in range(2,num) if num % x==0 ]

def primenum(n):
    if num>1:
        if(len(a))==0:
            print ('prime')
        else:
            print('not prime')
    else:
        print('Not prime')

primenum(num)


