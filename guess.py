from random import randint


def print_welcome():
    print("\n"*2 + " "*30 + "This is \"Guess the number\" game.\n")


def ask_level():
    level_selected = int(input("Please select difficulty level: 1(range 1:10) or 2(range 1: 100)\n"))
    return level_selected


def level(lvl_num):
    if lvl_num == 1:
        lower_bound = 0
        high_bound = 10
        max_attepmt = 4
    elif lvl_num == 2:
        lower_bound = 0
        high_bound = 100
        max_attepmt = 10
    else:
        raise TypeError
    print('You have {} attempts to guess what is the number Watson generated'.format(max_attepmt))
    return (randint(lower_bound, high_bound), max_attepmt)


def main_logic(inn):
    number = inn[0]
    max_attepmt = inn[1]
    attempts = 0

    while attempts < max_attepmt:
        user_input = input("enter your number:\n")
        attempts += 1
        if user_input == str(number):
            print("Congrats! you are correct!!")
            break
        elif user_input > str(number):
            print('Too high!')
        elif user_input < str(number):
            print('Too low!')
        if attempts == max_attepmt:
            print('Game Over. The number was {} '.format(number))
            break


print_welcome()
level_selected = ask_level()
num_for_lvl = level(level_selected)
main_logic(num_for_lvl)
