import random

word_list = ["aardvark", "baboon", "camel"]
randomword = random.choice(word_list)
print(randomword)
guess = input("Please guess a letter ").lower()
tally = 0;
for element in randomword:
  #print (element)
  if guess == element:
    tally += 1
  
if tally > 1:
  print("letter guessed was matched " + str(tally) + " times")
if tally == 0:
  print("letter was not a match")
