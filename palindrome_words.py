def compare_words(word):
    
    word_back = word[::-1]    
    
    if word_back.upper() == word.upper():
        return True
    else:
        return False

def run():
    word = str(input('Insert your word to compare: '))
    
    if compare_words(word):
        print('you word is a palindrome')
    else:
        print('you word is NOT a palindrome')
             

if __name__ == '__main__':
    run()