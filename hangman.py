import random

IMAGES = ['''

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
    |   |if __name__ == '__main__':
    run()

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']


WORDS = [
    
    'fornite',
    'minecraft',
    'callofduty',
    'activision',
    'apex'
]

def random_word():
    random_index = random.randint(0, len(WORDS) - 1)
    return WORDS[random_index]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * ---')     



def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Insert words : '))
        
        letter_indexes = []
        
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('sorry, the correct word is : {}'.format(word))
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
            
            letter_indexes =  []
        try:    
            hidden_word.index('-')             
        except ValueError:
            print('')
            print("YEAH YOU WON, THE CORRECT WORD IS : {}".format(word))  
            break  
                

if __name__ == '__main__':
    print('W E L C O M E  T O  H A N G M A N')
    run()