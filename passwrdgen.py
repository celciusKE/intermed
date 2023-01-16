#generate random numbers
import random
import array
#mix uppercase and lowercase
# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
MAXLEN=12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
#combine arrays the numbers and letters
digitmix=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS

#pick random numbers and letters
randnum = random.choice(DIGITS)
randupper = random.choice(UPCASE_CHARACTERS)
randlower = random.choice(LOCASE_CHARACTERS)
randsym = random.choice(SYMBOLS)

#combine random numbers and letters
temp_pswd = randnum+randlower+randupper+randsym

#temp_pswd contains 4 characters fill in the rest by selecting randomly from digitmix
for i in range(MAXLEN -4):
    temp_pswd2= temp_pswd+random.choices(str(digitmix))
    #convert temp_pswd to array and shuffle
    temp_pswd2list = array.array('u',temp_pswd2)
    random.shuffle(temp_pswd2list)
#traverse temp_pswd2list and append the chars to form password
password =""
for x in temp_pswd2list:
    password = password+x

print(password)