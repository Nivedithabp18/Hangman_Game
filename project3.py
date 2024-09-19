import random
import hangman_stages
print("Let's Play Hangman!!\n")
print("You Have Only 6 Lives.So Try To Guess The Word With In 6 Attempts.Good Luck!!\n")

word_list = ["apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry", "blueberry", "watermelon", "peach", "kiwi", "papaya", "cherry", "plum", "pear", "pomegranate", "lemon", "lime", "coconut", "fig"
]
chosen_word = random.choice(word_list)
display = []
for i in range(len(chosen_word)):
     display += '_'
print(display)
game_over = False
lives = 6

while not game_over:
     guessed_letter = input("Guess a letter:").lower()
     for position in range(len(chosen_word)):
         letter = chosen_word[position]
         if letter == guessed_letter:
            display[position] = guessed_letter
     print(display)
     
     if guessed_letter not in chosen_word:
         lives = lives - 1
         if lives == 0:
            print("You lose!! The word was:", chosen_word)
            game_over = True
     if '_' not in display:
         print("You won the match")
         game_over = True
       
     print(hangman_stages.stages[lives])
