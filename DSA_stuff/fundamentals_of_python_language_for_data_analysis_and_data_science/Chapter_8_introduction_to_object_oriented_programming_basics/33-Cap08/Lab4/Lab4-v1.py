# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========\n''', 

'''
+---+
|   |
O   |
    |
    |
    |
=========\n''', 

'''
+---+
|   |
O   |
|   |
    |
    |
=========\n''',

'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========\n''', 
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========\n
''', 

'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========\n''', 
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========\n''']


# Classe
class Hangman:

     correct_letters = []
     wrong_letters = []
     
     word_to_guess = []
     field_to_guess = []

	# Método Construtor
     def __init__(self):
          self.words = ["apple", "car"]
          
          self.next_word()
     
     # Method to select the next word in the game
     def next_word(self):

          self.choice = random.choice(self.words)

          self.words.remove(self.choice)
          self.word_to_guess = [letter for letter in self.choice]
           
          self.field_to_guess = ["_" for letter in self.choice]
          
          self.correct_letters = []
          self.wrong_letters = []
          
	# Método para adivinhar a letra
     def guess_the_letter(self, letter):

          # Check if the letter is in the word
          if letter in self.word_to_guess:
               # A loop in case there are more than one of the same letter
               while True:
               
                    # Save the corret letters in a list
                    self.correct_letters.append(letter)
                    
                    # The position index of the letter
                    index = self.word_to_guess.index(letter)

                    print("len words: ", len(self.words))

                    # Remove the letter from to word
                    # self.word_to_guess.remove(letter)
                    # del self.word_to_guess[index]
                    self.word_to_guess[index] = 1
                    
                    # Remove one of the '_'
                    self.field_to_guess.remove('_')
                    
                    # Add in the field the letter instead of a '_'
                    self.field_to_guess.insert(index, letter)
          
                    if letter not in self.word_to_guess:
                         break
          
          else:
               # Save the wrong letters in a list
               self.wrong_letters.append(letter)
               
               # Call the not_show_letter method and pass the quantity of wrong_letters -1 because the first index in a list is 0
               self.not_show_letter(len(self.wrong_letters) - 1)

          # Check if the game ended
          self.check_game_ended()
     
	# Método para verificar se o jogo terminou
     def check_game_ended(self):
          
          if len(self.words) == 0 and len(set(self.word_to_guess)) == 1:
               return True
          
          elif len(set(self.word_to_guess)) == 1:
               self.player_won()
               return False
          
          return False
	# Método para verificar se o jogador venceu
     def player_won(self):
          
          self.next_word()
          print("\nCongratulations you guessed correctly the first word!!")
          print("Let's go to the next one!!!\n")
               
	# Método para não mostrar a letra no board
     def not_show_letter(self, index):
          
          print(board[index])
     
     # Method to show the letter on the board
     
	# Método para checar o status do game e imprimir o board na tela
     def check_game_status(self):
          if self.player_won():
               return True
          
          return False
     
     def menu(self):
          print(self.field_to_guess)
          print("\nTry to guess the letter!")
          print("Type the letter: ")

def main():
     hangman_game = Hangman()

     while not hangman_game.check_game_ended():
          
          hangman_game.menu()
          
          letter = input("")
          
          hangman_game.guess_the_letter(letter)
     
     
     print("\nCongratulations you guessed correctly all the words!!!")
     
if __name__ == "__main__":
     main()
     
