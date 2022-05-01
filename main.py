# Libraries
import time
# Variables
start = input("Please press Enter to start!")
name_tycoon = input("What would you like to name your tycoon? ") 
i = 1
gen_2 = False
# Tycoon
if name_tycoon:
  print("You have been given Gen-1")
else:
  print("Invalid string or integer.")
  
print("Generator List:\nGen-1(FREE)\nGen-2($50)\nGen-3($1000)")

commands = input("What commands would you like to do (type 'help' for commands)? ")

if commands == ("help"):
  print("Commands:\nBuy - Buys a generator if you have enough cash.\nQuit - Quits the tycoon.\nList - Prints the generator list")

money = 0
while i > 0:
  time.sleep(10)
  money += 1
  print(money)
  n = input("Commands (Use only if you have enough money): ")
  if n == ("buy Gen-2"):
    if money == 50:
      print("You bought Gen-2")
      money += 5
      if money == 1000:
        print("You bought Gen-3")
        money += 100