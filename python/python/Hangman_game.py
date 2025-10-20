HANGMANPICS = ['''
    +---+
        |
        |
        |
        |
        |
  =========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random
words = ["bad", "moon", "beans" ]
random_word = random.choice(words)

display = ["_"] * len(random_word) 
print(" ".join(display))
lives = 5

guessed_list =[]
print(HANGMANPICS[0])
while "_" in display and lives > 0:
  guessed = input("Gusse thr letter: ").lower()
  if guessed in guessed_list:
    print("you have enterd this letter befor.")
    print(f"you have {lives} more left")
    continue 
  else:
    guessed_list.append(guessed)

  if guessed not in random_word:
    lives -= 1
    print(HANGMANPICS[6-lives])
  else:
    for place in range(len(random_word)):
      if random_word[place] == guessed:
        display[place] = guessed

  print(" ".join(display))
  print(f"you have {lives} more left")

if lives == 0:
  print(f"***you lose***")
  print(HANGMANPICS[-1])
else:
  print("***you win***")