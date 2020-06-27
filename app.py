import random

run_again = "Y"
print('***Dice Simulation***')
while run_again == "Y":

    number = random.randint(1, 6)

    if number == 1:
        print('''
        ----------
        |         |
        |    o    | 
        |         |
        ----------
        ''')

    if number == 2:
        print('''
        ----------
        |    o    |
        |         | 
        |    o    |
        ----------
        ''')

    if number == 3:
        print('''
        ----------
        |    o    |
        |    o    | 
        |    o    |
        ----------
        ''')

    if number == 4:
        print('''
        ----------
        | o     o |
        |         | 
        | o     o |
        ----------
        ''')

    if number == 5:
        print('''
        ----------
        | o     o |
        |    o    | 
        | o     o |
        ----------
        ''')

    if number == 6:
        print('''
        ----------
        | o     o |
        | o     o | 
        | o     o |
        ----------
        ''')

    run_again = input('roll again(Y or N) ').upper()


