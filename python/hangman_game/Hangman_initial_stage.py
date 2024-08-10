import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["program", "revere", "henry"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_start = True  #start the game
stored = []
lives = 6

while game_start :
        guess = input("Guess a letter: ").lower()
        if guess not in stored:
                stored.append(guess)
        display = ""
        for letter in chosen_word:
            if letter in stored:
                display += letter
            else:
                display += "_"
        new_display = display
        print(new_display)

            
        if guess not in chosen_word:
            print(stages[lives - 1])
            lives -= 1
            
        elif guess in chosen_word :
            print(stages[lives])
            
        if "_" not in new_display:
            game_start = False
            print("You win.")
        if lives == 0:
            game_start = False
            print("You lose")
