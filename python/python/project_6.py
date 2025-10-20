print("Welcome to Ishop calculator: ")
Number = int(input("Who many items are there in the basket: "))
cost = []
Items = []
# step 1:
print("letis get to countinig them:")
if Number > 0 :
  for list in range(1,Number+1):
    item_1 = input(f"Please tell me the name of the item number {list}: ")
    Items.append(item_1)
    price = float(input(f"What is the price of {item_1}:\n $"))
    cost.append(price)
  # step 2: Do you want to now the items in the basket.
  Answer_1 = input("Do you want to now the items in the basket? (yes/no)\n").lower()
  if Answer_1 =="yes" :
    print(Items)
    Answer_2 = input("Do you want to now the price of the items in the basket?(yes/no)\n").lower()
    if Answer_2 =="yes" :
      print(sum(cost))
    else :
      print("Fuck you \nWhy did you start, you idiot?")

  else :
    print("ok")
  # step 2: Do you want to now the total price.
else :
  print("Seema like you are not in the mood to shopping today." )