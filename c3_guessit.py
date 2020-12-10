import random
import sys


def gameMode():
    while True:
        try:
            difficulty = int(input(
                'Chose the game difficulty:\n1.SpongeBob (easy)\n2.Kratos (advanced)\n--> '))
            if difficulty in [1, 2]:
                print("\nNice let's start\n")
            else:
                difficulty = random.randint(1, 2)
                print('''WRONG!!, that is NOT an option,
                        \nI'll chose for you then...
                        \nGame Mode: {}\n'''.format(difficulty))
            return difficulty
        except ValueError:
            print('\nEnter only numbers, try again.\n')


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


def loser():
    messages = [
        "Nice try, you failed miserably!!",
        "Oh, C'mon!!!",
        "Stop Wasting my time...",
        "I can be here the whole day",
        "How many times are you gonna fail?",
        "You love ashaming yourself, don't you?",
        "Fail, fail, fail",
        "If you guess it right i'll tell you a secret",
        "The cake is a lie",
        "LOSER!!",
        "I am done with you",
        "There are only two infinite things, the universe, and the number of times you'll fail, and i am still not sure about the first one",
        "Hello, Mr. failure! :P"
    ]
    ran_msg = random.randint(0, len(messages) - 1)
    print('\n'+messages[ran_msg]+'\n')


def numPicker():
    mode = gameMode()
    n_range = numRange()
    rand_number = random.randint(n_range[0], n_range[1])
    while True:
        your_number = int(input('--------------\nPick a number '))
        try:
            if mode == 1:
                if your_number != rand_number:
                    loser()
                else:
                    print('\nNice, you got it!!')
                    break
            elif mode == 2:
                rand_number = random.randint(n_range[0], n_range[1])
                if your_number != rand_number:
                    print('\nThe right number was: {}'.format(rand_number))
                    loser()
                else:
                    print('\nNice, you got it!!')
                    break
        except ValueError as err:
            print(
                '\n{} - Enter only numbers, try again.\n'.format(type(err)))


try:
    numPicker()
except KeyboardInterrupt:
    print('\n\nBye!!!!!\n')

# messages to display if lose
# action if win
