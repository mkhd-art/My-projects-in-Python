tasks_finished=[]
tasks_not_finished=[]

names = input("Enter your tasks for today separated by commas: ").split(", ")
for name in names:
  print(f"{name}\n")
  answer = input(f"Do you finish {name}? (yes or no): ").lower()
  if answer == "yes":
    print("Nice jop!")
    tasks_finished.append(name)
  elif answer == "no" :
    print("Try not to put it off")
    tasks_not_finished.append(name)
  else :
    print("Invalid choice \n please inter (yes or no)")
  print("---------- \n")
  # Step = Do you want to see your progress? 
answer = input("Do you want to now your progress? (yes/no):").lower()
if answer =="yes" :
 print(f"tasks Finished: {tasks_finished}\ntasks not Finished: {tasks_not_finished}")
elif answer == "no":
  print("Thanks for using our program")
else :
  print("Invalid choice \n please inter (yes or no)")


#المشروع الثاني(انشاء كلمه سر عشوائيه)

import string
import random
#رساله ترحيبيه
welcome = print("Welcoe to the password generator!")
#طلب من المستخدم كم حرف يريده
Total_numbers_of_password = int(input("Inter the total number of the characters in the password: "))
Total_numbers = int(input("Enter the number or numbers in the password: "))
Total_letters = int(input("Enter the number or letters in the password: "))
Total_symbols = int(input("Enter the number or symbols in the password: "))
Total = sum([Total_numbers, Total_letters, Total_symbols])
#نتحقق من الحروف والارقام والعلامات
if Total != Total_numbers_of_password:
  print("The total number of characters in the password is less than the number of characters you entered. Please try again.")

else:
  password = (random.choices(string.digits, k=Total_numbers) +
   random.choices(string.ascii_letters, k=Total_letters) +
   random.choices(string.punctuation, k=Total_symbols))
#نلخبط الباسورد ونفصله عن بعض
  random.shuffle(password)
  password_2 = "".join(password)
#نطبع النتيجه الأخيره
  print(f"your password is: {password_2}")