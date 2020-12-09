import random
#number_try = input('Pick the numbers of attempts to try: ')


def gameMode():
    while True:
        difficulty = input(
            'Chose the game difficulty:\n1.SpongeBob (easy)\n2.Kratos (advanced)\n--> ')
        try:
            if int(difficulty) in [1, 2]:
                print("\nNice let's start\n")
            else:
                difficulty = random.randint(1, 2)
                print('''WRONG!!, that is NOT an option,
                        \nI'll chose for you then...
                        \nGame Mode: {}\n'''.format(difficulty))
            return difficulty
        except ValueError:
            print('\nEnter only numbers, try again.\n')


print(gameMode())


def numRange():
    while True:
        number_range = input(
            'Pick the range of numbers to guess separated by comma: ')
        try:
            if len(number_range.split(',')) == 2:
                if int(number_range.split(',')[0]) < int(number_range.split(',')[1]):
                    num1 = int(number_range.split(',')[0])
                    num2 = int(number_range.split(',')[1])
                elif int(number_range.split(',')[0]) > int(number_range.split(',')[1]):
                    num1 = int(number_range.split(',')[1])
                    num2 = int(number_range.split(',')[0])
            return num1, num2
        except ValueError as err:
            print(
                '\n{} - Enter only numbers, try again.\n'.format(type(err)))
        except UnboundLocalError as err:
            print(
                '{} - Values dont meet valid criteria:\n- 2 DIFFERENT values\n- Separated by a comma(,)\ntry again.\n'.format(type(err)))
