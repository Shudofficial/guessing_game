#this products demonstrates a guessing game
from random import randint

playername= input("Enter your name ")
print("hello there "+ playername +"!")
#using while loop
number = randint(10, 50)

counter=0
while counter < 5:
    number=eval(input("Enter your number"))

# getattrgenerate a random number
# then check if a number is equal to generated number 
# using a while...loop check whether the user input is equal to the generated number


