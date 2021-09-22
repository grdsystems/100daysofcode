print("Welcome to Money Bag Island \n")
print("Your mission is to find that $$$BAG$$$ \n")
print("You are at a cross road.  Where do you want to go? ")
lifechoice1 = input("Enter \"left\" to procrastinate or \"right\" to keep going \n")

if (lifechoice1 == "right"):
    print("You come to a lake.  There is an island in the middle of the lake. \n")
    lifechoice2 = input("Type \"wait\" to wait for a boat.  Type \"swim\" to swim across. \n")
    if (lifechoice2 == "swim"):
         print("You arrive at the island tired and hungry\n")
         lifechoice3 = input("There is a house with 3 doors.  One red, one yellow and one blue.  Which color do you choose? \n")
         if lifechoice3 == "yellow":
             print("Bag found, you are rich")
         else:
             print("Game Over")
    else: 
        print("No Bag for you")
else:
    print("No Bag for you")




















# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()
# true = 0
# love = 0
# T = name1.count("t") + name2.count("t")
# print(f"T occurs {T} times")
# true += T
# R = name1.count("r") + name2.count("r")
# print(f"R occurs {R} times")
# true += R
# U = name1.count("u") + name2.count("u")
# print(f"U occurs {U} times")
# true += U
# E = name1.count("e") + name2.count("e")
# print(f"E occurs {E} times")
# true += E
# print("Total = " + str(true))

# L = name1.count("l") + name2.count("l")
# print(f"L occurs {L} times")
# love += L
# O = name1.count("o") + name2.count("o")
# print(f"O occurs {O} times")
# love += O
# V = name1.count("v") + name2.count("v")
# print(f"V occurs {V} times")
# love += V
# E = name1.count("e") + name2.count("e")
# print(f"E occurs {E} times")
# love += E
# print("Total = " + str(love))

# total_score = int(str(true) + str(love))
# print(f"Love Score = {total_score}")

# if total_score < 10 or total_score > 90:
#     print(f"Your score is {total_score}, you go together like coke and mentos")
# elif total_score > 40 and total_score < 50:
#     print(f"Your score is {total_score}, you are alright together.")
# else:
#     print(f"Your score is {total_score}")


# print("Welcome to Python Pizza Deliveries")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: " )
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#   bill = 15
# elif size == "M":
#   bill = 20
# else:
#   bill = 25
# if size == "S" and add_pepperoni == "Y":
#     bill +=2
# else:
#   bill +=3
# if extra_cheese == "Y":
#   bill +=1
# print(f"Your final bill is: ${bill}")


# year = int(input("Which year do you want to check?\n"))
# if year % 4 == 0 and year % 100 != 0:
#   print("Leap")
# elif year % 400 == 0:
#   print ("Leap")
# else:
#   print("Not Leap")


# number = int(input("which number do you want toc check? "))

# if (number % 2) == 0:
#   print("This is an even number")
# else:
#   print("This is an odd number")

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# bmi = round(weight/height **2)

# if bmi < 18.5 :
#   print("underweight")
# elif bmi < 25:
#   print("normal")
# elif bmi < 30:
#   print("overweight")
# elif bmi < 35:
#   print("obese")
# else:
#   print("clinically obese")
