What is Hangman Game?
	Hangman is a classic word-guessing game.The player must guess a hidden word, one letter at a time.•	For each incorrect guess, a part of a hangman figure (head, body, arms, legs) is drawn.	The goal is to guess the word before the hangman figure is fully drawn.	Players lose if the figure is completed before the word is guessed.

How Hangman Game in Python Works
   1.Word List & Random Selection: A list of words is defined, and Python's random.choice() selects a word for the player to guess.
   2.User Interaction: The player inputs guesses using the input() function, and the game evaluates them.
   3.Lives System: The player has 6 lives, and each wrong guess reduces the number of lives, bringing the player closer to losing.
   4.Hangman Figure: The game visualizes the hangman figure step by step, starting from an empty gallows and progressively adding parts based on incorrect guesses.
   5.Win/Lose Conditions: The player wins if they guess the word correctly before all lives are lost, or loses if the hangman figure is fully drawn.

	  Word Selection and Initial Setup 
1. import random - This imports the random module, which provides various functions for generating random numbers. In this case, we will use it to randomly select a word from a predefined list. 
2. import hangman_stages - This imports another Python file (hangman_stages.py) that contains the visual stages of the Hangman game. It helps display the hangman diagram as the player guesses incorrectly.
3. word_list = ["apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry", "blueberry", "watermelon", "peach", "kiwi", "papaya", "cherry", "plum", "pear", "pomegranate", "lemon", "lime", "coconut", "fig"] - This defines a list of words (fruits in this case) from which the game will randomly select one for the player to guess. The list is stored in a variable named word_list.
4. chosen_word = random.choice(word_list) - This line selects a random word from the word_list using the random.choice() function. The selected word is stored in the variable chosen_word, which will be the word the player tries to guess.
5. print(chosen_word) - This temporarily prints the chosen_word to the console. It's usually used for debugging purposes, so you may want to remove it later to avoid revealing the word to the player.
6. display = [] - This initializes an empty list named display. This list will eventually hold the guessed letters or underscores ( _ ) to represent the word the player is trying to guess.
7. for i in range(len(chosen_word)): - This line begins a loop that will iterate over the length of the chosen_word. len(chosen_word) gives the number of characters in the word, and range(len(chosen_word)) creates a sequence of numbers from 0 to the length of the word minus one.
8. display += '_' - For each character in the chosen word, this line adds an underscore ( _ ) to the display list. This is done because, at the start of the game, none of the letters have been guessed yet, so the word is represented entirely by underscores.
9. print(display) - This prints the initial display list to the console. It will look something like ['_', '_', '_', '_', '_'] if the chosen word has 5 letters. The underscores represent the hidden letters that the player must guess.
10. game_over = False - This initializes a boolean variable game_over and sets it to False. This variable will control when the game ends. The game will continue as long as game_over is False.
11. lives = 6 - This sets the number of lives the player has. Each time the player guesses a letter incorrectly, one life is subtracted. The player loses the game when they run out of lives (i.e., when lives becomes 0). Six lives correspond to the 6 stages of the hangman.

    Input Handling and Letter Checking
1. while not game_over: - This starts a while loop that will continue to run as long as the variable game_over is False. This loop is the core of the game and repeats until the game ends (either when the player wins or loses).
2. guessed_letter = input("Guess a letter: ").lower() - This line prompts the player to guess a letter. The input() function asks the player for input, and lower() converts the input to lowercase to ensure the game is case-insensitive.The guessed letter is stored in the variable guessed_letter. This will be used to check if the letter is in the chosen word.
3. for position in range(len(chosen_word)): - This begins a for loop that iterates through each position (index) in the chosen_word. The range(len(chosen_word)) generates a sequence of numbers corresponding to the indices of the letters in the word (from 0 to the length of the word minus one).
4. letter = chosen_word[position] - For each iteration of the loop, this line assigns the current letter of the chosen_word (at index position) to the variable letter. So, for example, if the word is "apple," the loop will assign letter to "a," then "p," then "p," and so on.
5. if letter == guessed_letter: - This checks if the current letter (from the word) matches the player's guessed_letter. If they are the same, it means the player guessed a correct letter.
6. display[position] = guessed_letter - If the guessed letter is correct, this line updates the display list by replacing the underscore (_) at the correct position with the guessed letter. This way, the player can see their correct guess in the word's displayed representation.For example, if the word is "apple" and the player guesses "p," the display might change from ['_', '_', '_', '_', '_'] to ['_', 'p', 'p', '_', '_'].
7. print(display) - This prints the updated display list to the console, allowing the player to see their progress after each guess. The display will show the correct letters guessed so far and underscores for the remaining hidden letters.

     Life Management and Game Over Condition
1. if guessed_letter not in chosen_word: - This checks whether the guessed_letter is not in the chosen_word. If the letter is not present, it means the player guessed incorrectly, and they will lose a life.
2. lives = lives - 1 - 	If the guessed letter is not in the word, this line subtracts 1 from the lives variable. This decreases the number of remaining attempts the player has. The game starts with 6 lives, so each incorrect guess reduces the number of lives by 1.
3. if lives == 0: - 	This checks whether the player has run out of lives (i.e., if lives is equal to 0). If this condition is met, the game is over because the player has exhausted all their chances.
4. game_over = True - If the player has no lives left, this line sets the game_over variable to True, which will break the while loop (from Participant 2's section) and stop the game.
5. print("You lose!!") - 	If the game ends because the player has run out of lives, this line prints a message, "You lose!!", informing the player that they’ve lost the game.
6. if '_' not in display: - This checks whether there are no underscores left in the display list. If the player has guessed all the letters correctly (and there are no more hidden letters), the game ends and the player wins.
7. game_over = True - If there are no underscores in the display, this line sets game_over to True, stopping the while loop and ending the game because the player has successfully guessed the word.
8. print("You win") - 	If the player has guessed all the letters correctly, this line prints a message, "You win", informing the player that they’ve won the game.

     Hangman Stages
1.import hangman_stages - imports the hangman stages from another Python file. These stages visually represent the progress of the game based on how many wrong guesses have been made.   
2.print(hangman_stages.stages[lives] - This line prints the current visual representation of the hangman. The lives variable acts as an index to access the correct stage from the stages list in hangman_stages.py. As lives decrease, the hangman drawing becomes more complete, eventually showing a fully drawn figure when the player loses.

 

