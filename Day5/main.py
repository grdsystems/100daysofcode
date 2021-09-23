#For Loop with Range

#for number in range(1, 11, 3):
  #print(number)

# total = 0
# for number in range(1, 101):
#   total+=number

# print(total)
#total = 0
#for number in range(2, 101, 2):
  #total += number
#print(total)


# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 5 == 0:
#     print ("Buzz")
#   elif number % 3 == 0:
#     print ("Fizz")
#   else:
#     print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for n in range (1, nr_letters+1):
#   password+=random.choice(letters)
# for n in range (1, nr_symbols+1):
#   password+=random.choice(symbols)
# for n in range (1, nr_numbers+1):
#   password+=random.choice(numbers)

# print ("Easy " + password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = []
randompassword = ""
for n in range (1, nr_letters+1):
  password2.append(random.choice(letters))
for n in range (1, nr_symbols+1):
  password2.append(random.choice(symbols))
for n in range (1, nr_numbers+1):
  password2.append(random.choice(numbers))
random.shuffle(password2)
for y in password2:
  randompassword += y
print(f"Your password is: {randompassword}") 

