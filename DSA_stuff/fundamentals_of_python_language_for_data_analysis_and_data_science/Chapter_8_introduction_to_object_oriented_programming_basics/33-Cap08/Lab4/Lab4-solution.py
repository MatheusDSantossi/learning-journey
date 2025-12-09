# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Function to clean the screen in each exectuion
def clean_screen():
    # Windows
    if name == "nt":
        _ = system("cls")
    # Mac or Linux
    else:
        _ = system("clear")

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', 

'''
+---+
|   |
O   |
    |
    |
    |
=========''', 

'''
+---+
|   |
O   |
|   |
    |
    |
=========''',

'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', 
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''', 

'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', 
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:

	# Método Construtor
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.chosen_letters = []
    
	# Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.chosen_letters:
            self.chosen_letters.append(letter)
            
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
            
        else: 
            return False
        
        return True
     
	# Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.wrong_letters) == 6)

	# Método para verificar se o jogador won
    def hangman_won(self):
        if "_" not in self.hide_word():
            return True
        return False
     
	# Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ""
        
        for letter in self.word:
            if letter not in self.chosen_letters:
                rtn += "_"
            else:
                rtn += letter
                
        return rtn
    
	# Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.wrong_letters)])
        
        print("\nWord: " + self.hide_word())
        
        print("\nWrong letters: ", )
        
        for letter in self.wrong_letters:
            print(letter,)
            
        print()
    
# Method to randomly read a word from the word database
def rand_word():
    # List of words for the game
    words = ["banana", "avocado", "grape", "strawberry", "orange"]
    
    # Randomly chose one word
    word = random.choice(words)
    
    return word
        
def main():
    clean_screen()
    
    # Create the object and randomly select a word
    game = Hangman(rand_word())
    
    # While the game doesn't finish, print the status, require a letter and do the character scan
    while not game.hangman_over():
        # Game status
        game.print_game_status()
        
        # Receive the input from the terminal
        user_input = input("\nType a letter: ")
        
        # Check if the letter typed is part of the word
        game.guess(user_input)
        
    # Check the game status
    game.print_game_status()
    
    # Following the status, print the message on the screen for the user
    if game.hangman_won:
        print("\nCongratulations! You won!!")
    else:
        print("\nGame over! You lost!!")
        print("\nThe word was: ", game.word)
        
    print("\nIt was good play with you! Now go to study more!!")

if __name__ == "__main__":
    main()
