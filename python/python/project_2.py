print("Welcom to my isiLand!")
print("there are two doors in front of you. a Red  door and a Blue  door")
Door = input("Which door do you want to open? \n" ).lower()
if Door == "red":
 print("Great, you now entered a room")
 print("You found three boxes: White, Green, yellow")
elif Door == "blue" :
 print("you choose the bats door \n Game Over  X X ")
else :
 print("Worng choice \n Plese choose (Red or Blue)")

Box = input("which box do you open? \n").lower()
if Box == "green" :
 print("Congratulations, you found my treasure ")
elif Box == "yellow" :
 print("Oops you opend a box with Scorpions ")
elif Box == "white" :
 print("Oops, you opend a box filled with snakes ")
else:
 print("Wrong choice\n Plese choose (Green, White or Yellow)")