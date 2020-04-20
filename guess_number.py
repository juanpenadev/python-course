import random

def run():
    number_found = False
    random_number = random.randint(0, 20)
    
    while not number_found:
        number = int(input('Try a number: '))
        
        if number == random_number:
            print('yeahh is the right number')
            number_found = True
        elif number < random_number:
            print('your number is less than the correct one')
        else:
            print('your number is more than the correct one')
                

if __name__ == '__main__':
    run()