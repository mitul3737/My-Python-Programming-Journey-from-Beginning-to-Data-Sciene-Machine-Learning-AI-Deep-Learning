import random

number=random.randint(1,100)
attempts=0

while True:
    input_number=int(input("Guess the number between 1 to 1000"))
    attempts+=1

    if input_number==number:
         print("Yes,you are right")
         break
    if input_number>number:
         print("Incorrect!Please try to guess a smaller number")
    else:
         print("Incorrect!Please try to guess a larger number")

print("You tried ", attempts," times to find the correct number")