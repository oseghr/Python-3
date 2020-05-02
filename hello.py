# this program says hello and ask for name

print("Hello World!")
print("What is your name?")

myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
print("what is your age?")

myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

password = "swordfish"
if password == "swordfish":
    print("Access granted")
else:
    print("wrong password")

spam = 0
while spam < 10:
    print("Hello Ose")
    print(spam)
    spam += 1

spam = 0
for num in range(101):
    spam += num
print(spam)

import sys
print("Hello")
sys.exit()
print("goodbye")    
 
