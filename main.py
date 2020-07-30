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

print("welcome to Marvel Heroes Quiz\n")

name = input("Hello what is your name? \n")
answer = input("Hello " + name + "! Ready to play? Y or N \n")
print()


if answer.upper() == "Y":
  print("Play game")
  ok = 0
  while ok == 0:
    q1 = input("What color would you choose? (Choose A, B, C or D ) \nA) Blue \nB)Red \nC)Green \nD)Purple \n ")
    if q1.upper() in ("A", "B", "C", "D"):
      ok = 1
    else:
      print("focus please! A, B, C or D")
        
  fine = 0
  while fine == 0:
    q2 = input("What sport do you prefer? (choose A or B) \nA) Soccer(Football) \nB) Tennis \n ")
    if q2.upper() in ("A", "B"):
      fine = 1
    else:
      print("pay attention to the question")

  well = 0
  while well == 0:
    q3 = input("What game do you prefer? (choose A or B) \nA) Mincraft \nB) Fortnite \n ")
    if q3.upper() in ("A", "B"):
      well = 1
    else:
      print("pick A or B")

  choice = q1 + q2 +q3

  wait = input("Do you want to know your marvel hero?: ")
  
  
  print("Your Marvel hero is " + Heroes[choice.upper()])

if answer.upper() == "N":
  