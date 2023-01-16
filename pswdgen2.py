import random
import string

def pswd_gen(size=8,chars=string.ascii_letters+string.digits+string.punctuation):
    return ''.join(random.choice(chars)for x in range(size))

print(pswd_gen(int(input("How many characters do you want in your passwd: "))))