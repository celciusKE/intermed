#user gives string
name = input("Give me a string: ")

#covert string to a list
name=str(name)

#reverse the name
reverse = name[::-1]


#is string palindrome
if name== reverse:
    print("This is a Palindrome")
else:
    print("not a palindrome")
    
