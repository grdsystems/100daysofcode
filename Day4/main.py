# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
horizontal = int(position[0])
vertical = int(position[1])
# Write your code below this row 👇

map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# payer = random.randint(0, len(names)-1)

# print(f"{names[payer]} is going to pay")


#choose = input("What do you choose? Type 0 for Rock, 1 for scissor, 2 for paper: \n")


# import random
# import my_module

# c = random.randint(0, 1)

# if c == 1:
#   print("heads")
# else:
#   print("tails")
