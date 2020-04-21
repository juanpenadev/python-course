
def first_not_repeating_Char(char_sequence):
    
    seen_letters = {}
    
    for i, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (i, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1]+1)
    
    final_letters = []

    for key, value in seen_letters.items():

        if value[1] == 1:
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key = lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__ == '__main__':
    char_sequence = str(input('Write your char sequence: '))

    result = first_not_repeating_Char(char_sequence)

    if result == '_':
        print('All the char are repeating. ')
    else:
        print('the first not repeating char is: {}'.format(result))
