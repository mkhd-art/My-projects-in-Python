List = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
old = input("who old are you ?\n")
if old == "18" :
  # step 1 : print the game board
  print("Welcome to my Game: Place the Rabbit 🐇")
  print(f"{List[0]} \n{List[1]} \n{List[2]}\n")
  print("Where should the rabbit go? 🐇")
  # step 2 : ask the user to enter the row and column
  number = input("please choose a row and a column: \n")
  if number == [1,2,3] :
    raw = int(number[0])-1
    column = int(number[1])-1
    List[raw][column] = "🐇"
    # step 3 : print the final game board
    print("\nSuccess....\n")
    print(f"{List[0]} \n{List[1]} \n{List[2]}\n Have Fun 😊")
  else :
   print("Please enter a number from 1 to 3")
else :
  print("Sorry, you can't play this game \n You under 18 years old 😊")