#Greeting
print("Welcome to the tip calculator.\n")

#Inputs
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_of_people = int(input("How many people to split the bill? \n"))

#Calculations
tip_percentage = total_bill * (float(tip_percentage/100))
total_bill = total_bill + tip_percentage
split = round(total_bill/int(num_of_people), 2)

#Result
print(f"Each person should pay: {split}")

