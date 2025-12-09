# pseudocode (generated using ChatGPT)
# Início
#     // Inicialização
#     lista_de_palavras ← ["BRASIL", "COMPUTADOR", "PROGRAMACAO", "JOGADOR", ...]
#     palavra_secreta ← escolher_aleatoriamente(lista_de_palavras)
#     letras_adivinhadas ← conjunto vazio
#     tentativas_erradas ← 0
#     max_tentativas ← 6   // número máximo de erros permitidos

#     // Cria a representação inicial da palavra (underscores)
#     para cada letra em palavra_secreta faça
#         estado_atual ← estado_atual + "_ "
#     fim para

#     // Loop principal do jogo
#     enquanto (tentativas_erradas < max_tentativas) E (estado_atual contém "_") faça
#         exibir("Palavra: " + estado_atual)
#         exibir("Letras já tentadas: " + letras_adivinhadas)
#         exibir("Erros: " + tentativas_erradas + "/" + max_tentativas)
        
#         // Entrada do jogador
#         entrada ← ler_caractere("Digite uma letra: ")
#         letra ← converter_para_maiusculo(entrada)
        
#         se letra já estiver em letras_adivinhadas então
#             exibir("Você já tentou essa letra. Tente outra.")
#             continuar  // volta ao início do loop sem penalizar
#         fim se
        
#         adicionar letra a letras_adivinhadas
        
#         // Verifica acerto ou erro
#         se letra pertence a palavra_secreta então
#             // Atualiza estado_atual revelando todas as ocorrências da letra
#             novo_estado ← ""
#             para i de 1 até comprimento(palavra_secreta) faça
#                 se palavra_secreta[i] = letra então
#                     novo_estado ← novo_estado + letra + " "
#                 senão
#                     novo_estado ← novo_estado + estado_atual[2*i-1] + " "
#                 fim se
#             fim para
#             estado_atual ← novo_estado
#         senão
#             tentativas_erradas ← tentativas_erradas + 1
#             exibir("Letra incorreta!")
#         fim se
#     fim enquanto

#     // Verifica resultado final
#     se estado_atual não contém "_" então
#         exibir("Parabéns! Você ganhou!")
#         exibir("A palavra era: " + palavra_secreta)
#     senão
#         exibir("Você perdeu. Número máximo de erros atingido.")
#         exibir("A palavra era: " + palavra_secreta)
#     fim se
# Fim
# ```

# Import
import random
from os import system, name

# Function to clean the screen in each execution
def clean_screen():
    # Windows
    if name == "nt":
        _ = system('cls')
    
    # Mac or Linux
    else:
        _ = system('clear')

def display_hangman(opportunity):
    # List of the gallows stages
    stages = [
        # Stage 6 (final)
        """
        -------------
        |           |
        |           O
        |         \\| /
        |           |
        |          / \\
        |
        |
        _
        """,
        # Stage 5
        """
        -------------
        |           |
        |           O
        |         \\| /
        |           |
        |          / 
        |
        |
        _
        """,
        # Stage 4
        """
        -------------
        |           |
        |           O
        |         \\| /
        |           |
        |          
        |
        |
        _
        """,
        # Stage 3
        """
        -------------
        |           |
        |           O
        |         \\|
        |           |
        |          
        |
        |
        _
        """,
        # Stage 2
        """
        -------------
        |           |
        |           O
        |           |
        |           |
        |          
        |
        |
        _
        """,
        # Stage 1
        """
        -------------
        |           |
        |           O
        |           
        |           
        |          
        |
        |
        _
        """,
        # Stage 0
        """
        -------------
        |           |
        |           
        |           
        |           
        |          
        |
        |
        _
        """
    ]
    
    return stages[opportunity]

# Main function
def game():
    clean_screen()
    
    print("\nWelcome to hangman game!!")
    print("You need to guess the word:\n")
    
    # List of words for the game
    words = ["banana", "avocado", "strawberry", "grape", "pinneapple", "orange"]
    
    # Chose a random word
    word = random.choice(words)
    
    # List comprehension
    found_letters = [letter for letter in word]
    
    # Create the table with the character "_" multiplying by the length of the word
    table = ["_"] * len(word)
    
    # Numbers of opportunities
    max_opportunities = 10
    
    # List for the wrong letters
    wrong_letters = []
    
    while max_opportunities > 0:
        # Info
        print(" ".join(table))
        print("\nOpportunities left: ", max_opportunities)
        print("Wrong letters: ", " ".join(wrong_letters))
        
        # Try
        user_letter_try = input("\nType a letter: ").lower()
        
        if user_letter_try in word:
            index = 0
            for letter in word:
                if user_letter_try == letter:
                    table[index] = letter
                index += 1
            
            # If all the spaces were filled, the game is over
            if "_" not in table:
                print("\nYou won! The word was: ", word) 
                break
        else:
            print("Ops... This letter isn't in the word!!")
            max_opportunities -= 1
            wrong_letters.append(user_letter_try)
            
    # Condition
    if "_" in table:
        print("\nYou lost, the word was: ", word)


# Main block
if __name__ == "__main__":
    # game()
    x = "Data"
    print(x[:4])
    print("\nCongratulations. You are learning programmation in Python!! :)\n")