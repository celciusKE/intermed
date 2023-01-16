import random

s= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen=12

passwd = ''.join(random.sample(s,passlen))

print(passwd)