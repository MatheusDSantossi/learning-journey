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

     correct_letters = []
     wrong_letters = []
     
     word_to_guess = []
     field_to_guess = []

	# Método Construtor
     def __init__(self, words):
          self.words = words
          
          self.choice = random.choice(words)

          self.words.remove(self.choice)
          self.word_to_guess = [letter for letter in self.choice]
          self.field_to_guess = ["_" for letter in self.choice]
          
     def next_word(self):

          self.choice = random.choice(self.words)

          self.words.remove(self.choice)
          self.word_to_guess = [letter for letter in self.choice]
          self.field_to_guess = ["_" for letter in self.choice]
          
          self.correct_letters = []
          self.wrong_letters = []
          
	# Método para adivinhar a letra
     def guess_the_letter(self, letter):
                    
          # while not self.check_game_ended:
          if letter in self.word_to_guess:
               # print("letter: ", letter)
               # print("Letter in word")
               # print("Word to guess: ", self.word_to_guess)
               self.correct_letters.append(letter)
               
               index = self.choice.index(letter)
               # print("index: ", index)
               self.word_to_guess.remove(letter)
               self.field_to_guess.remove('_')
                              
               # print("field_to_guess: ", self.field_to_guess)
               self.field_to_guess.insert(index, letter)
               # print("field_to_guess: ", self.field_to_guess)
               
               print(self.field_to_guess)
               
          else:
               self.wrong_letters.append(letter)
               self.not_show_letter(len(self.wrong_letters) - 1)

          self.check_game_ended()
     
	# Método para verificar se o jogo terminou
     def check_game_ended(self):
          
          if len(self.words) == 0 and len(self.word_to_guess) == 0:
               print("Congratulations you guessed correctly all the words!!!")
               return True
          
          elif len(self.word_to_guess) == 0:
               self.player_won()
               return False
          
          return False
	# Método para verificar se o jogador venceu
     def player_won(self):
          
          self.next_word()
          print("Congratulations you guessed correctly the first word!!\n")
          print("Let's go to the next one!!!\n")
          print(self.field_to_guess)
               
	# Método para não mostrar a letra no board
     def not_show_letter(self, index):
          
          print(board[index])
          print(self.field_to_guess)
     
     # Method to show the letter on the board
     
	# Método para checar o status do game e imprimir o board na tela
     def check_game_status(self):
          if self.player_won():
               return True
          
          return False
     
     def menu(self):
          print("Try to guess the letter!")
          print("Type the letter: ")

if __name__ == "__main__":
     hangman_game = Hangman(["apple", "car"])
     
     while not hangman_game.check_game_ended():
          
          hangman_game.menu()
          
          letter = input("")
          
          hangman_game.guess_the_letter(letter)
     
