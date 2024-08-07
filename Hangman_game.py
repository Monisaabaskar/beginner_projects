import random

word_list = ["testimony", "revere", "encapsulation"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_start = True  #start the game
stored = []

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
         if not "_" in display:
            game_start= False
            print("won")