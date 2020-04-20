KEYS = {

    'a': '9',
    'b': '8',
    'c': '7',
    'd': '6',
    'e': '5',
    'f': '4',
    'g': '3',
    'h': '2',
    'i': '1',
    'j': 'z',
    'k': 'y',
    'l': 'x',
    'm': 'w',
    'n': 'v',
    'o': 'u',
    'p': 't',
    'q': 's',
    'r': 'r',
    's': 'q',
    't': 'p',
    'u': 'o',
    'v': 'n',
    'w': 'm',
    'x': 'l',
    'y': 'k',
    'z': 'j',
    '1': 'i',
    '2': 'h',
    '3': 'g',
    '4': 'f',
    '5': 'e',
    '6': 'd',
    '7': 'c',
    '8': 'b',
    '9': 'a',
    '0': '0',
    ' ': ' ',

}


def cypher(message):
    temp = ''
    for i in message:
        temp += KEYS[i]
    return temp


def decypher(message):
    temp = ''
    for i in message:
        for key, value in KEYS.items():
            if value == i:
                temp += key

def run():
    while True:
        print('')
        print('1 = encrypt ')
        print('')
        print('2 = decrypt ')
        print('')
        print('3 = exit')
        print('')
        pick = int(input("what would you like : "))
        print('')
        
        if pick == 3:
            break
        elif pick == 1:
            message = str(input('Insert your text : '))
            result = cypher(message)
            print("New message crypted: ", result)
        elif pick == 2:
            message = str(input('Insert your text : '))
            result = cypher(message)
            print("New message decrypted: ", result)
        else:
            break

if __name__ == '__main__':
    run()
