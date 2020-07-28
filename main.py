# result dictionary
Heroes = {
    "AAA" : "Starlord",
    "AAB" : "Drax",
    "ABA" : "Black Panther",
    "ABB" : "Doctor Strange",
    "BAA" : "Winter Soldier",
    "BAB" : "Rocket Raccoon",
    "BBA" : "Captain America",
    "BBB" : "Iron Man",
    "CAA" : "Groot",
    "CAB" : "Hulk",
    "CBA" : "Spiderman",
    "CBB" : "Mantis",
    "DAA" : "Thanos",
    "DAB" : "Thor",
    "DBA" : "Hawkeye",
    "DBB" : "Black Widow"
}

print("welcome to Marvel Heroes Quiz")

name = input("Hello what is your name? ")
answer = input("Hello " + name + "! Ready to play? Y or N")
print()
if answer.upper() == "Y":
  print("Play game")
  q1 = input("What color would you choose? (Choose A, B, C or D ) \nA) Blue \nB)Red \nC)Green \nD)Purple \n ")

  q2 = input("What sport do you prefer? (choose A or B) \nA) Soccer(Football) \nB) Tennis \n ")

  q3 = input("What game do you prefer? (choose A or B) \nA) Mincraft \nB) Fortnite \n ")

  choice = q1 + q2 +q3

  wait = input("Do you want to know your marvel hero?: ")
  
  
  print("Your Marvel hero is " + Heroes[choice.upper()])

if answer.upper() == "N":
  print("if you want to find your marvel super hero you must press Y and enter")

else:
  print("you must press Y or N")