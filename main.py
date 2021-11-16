### Describe each datatype below:(4 marks)

## 4         = integer
## 5.7       = float
## True      = boolean
## Good Luck = string

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer
# Integer
#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer
#String

####Create a variable tha will store the users name.(1 mark)
name = input("Enter your name: ")
print("Hi",name)
####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
print("This are the first 4 characters:",name[:4])

####Convert the user's name to all uppercase characters and print the result

print("This is your name is name in capital letters:",name.upper())

####Find out how many times the letter A occurs in the user's name
Count = name.count("a")
print("This is who many a are in your name:",Count)



#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
age = 0
age = int(input("Enter your age: "))
if age <= 18:
 print("You can't enter the competition")
elif age >= 18:
 print("You can enter the competition")

#### Create an empty list called squareNumbers (3 marks)

SquareNumbers = []


#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
for num in range(21):
  square = num * num
  SquareNumbers.append(square)

###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
print(SquareNumbers)

####Print your list (1 mark)

####Create a variable called userSquare that asks the user for their favourite square number
# userSquare = int(input("What is your favourite square number? "))
userSquare = int(input("What is your favourite square number?: "))


#### Add this variable to the end of your list called SquareNumbers
SquareNumbers.append(userSquare)
print(SquareNumbers)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
choice = SquareNumbers[random.randint(0,22)]
print(choice)
####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)

print("The random square number is:", choice)
