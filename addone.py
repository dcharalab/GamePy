import random
import keyboard
import os


def print_array(array):
    os.system('cls')
    for row in array:
        print(row)


def is_valid_to_proceed(x, y):
    if x > 4 or y > 4 or x < 0 or y < 0:
        return False
    else:
        return True


def initialize():
    x = random.randrange(5)
    y = random.randrange(5)
    return x, y


def move_left(array, start_x, start_y, x, y, start_num):
    old_y = start_y
    start_y = start_y - 1
    if is_valid_to_proceed(start_x, start_y):
        if x == start_x and y == start_y:
            array[start_x][start_y] = array[start_x][old_y] + 1
        else:
            array[start_x][start_y] = array[start_x][old_y]
        array[start_x][old_y] = 0
    else:
        start_y = start_y + 1
    return start_x, start_y, x, y


def move_backwards(array, start_x, start_y, x, y, start_num):
    old_x = start_x
    start_x = start_x + 1
    if is_valid_to_proceed(start_x, start_y):
        if x == start_x and y == start_y:
            array[start_x][start_y] = array[old_x][start_y] + 1
        else:
            array[start_x][start_y] = array[old_x][start_y]
        array[old_x][start_y] = 0
    else:
        start_x = start_x - 1
    return start_x, start_y, x, y


def move_forward(array, start_x, start_y, x, y, start_num):
    old_x = start_x
    start_x = start_x - 1
    if is_valid_to_proceed(start_x, start_y):
        if x == start_x and y == start_y:
            array[start_x][start_y] = array[old_x][start_y] + 1
        else:
            array[start_x][start_y] = array[old_x][start_y]
        array[old_x][start_y] = 0
    else:
        start_x = start_x + 1
    return start_x, start_y, x, y


def move_right(array, start_x, start_y, x, y, start_num):
    old_y = start_y
    start_y = start_y + 1
    if is_valid_to_proceed(start_x, start_y):
        if x == start_x and y == start_y:
            array[start_x][start_y] = array[start_x][old_y] + 1
        else:
            array[start_x][start_y] = array[start_x][old_y]
        array[start_x][old_y] = 0
    else:
        start_y = start_y - 1
    return start_x, start_y, x, y


def play_game():
    start_x, start_y = (0, 0)
    cols_count, rows_count = (5, 5)
    start_num = 1
    array = [[0 for x in range(cols_count)] for x in range(rows_count)]

    x, y = initialize()
    array[x][y] = start_num

    if x == start_x and y == start_y:
        array[start_x][start_y] = array[x][y] + start_num
        while x == start_x and y == start_y:
            x, y = initialize()
        array[x][y] = start_num
    else:
        array[start_x][start_y] = start_num

    while(True):
        print_array(array)

        if keyboard.read_key() == "a":
            start_x, start_y, x, y = move_left(array, start_x,
                                               start_y, x,
                                               y, start_num)
        elif keyboard.read_key() == "s":
            start_x, start_y, x, y = move_backwards(array, start_x,
                                                    start_y, x,
                                                    y, start_num)
        elif keyboard.read_key() == "w":
            start_x, start_y, x, y = move_forward(array, start_x,
                                                  start_y, x,
                                                  y, start_num)
        elif keyboard.read_key() == "d":
            start_x, start_y, x, y = move_right(array, start_x,
                                                start_y, x,
                                                y, start_num)

        if x == start_x and y == start_y:
            while x == start_x and y == start_y:
                x, y = initialize()
            array[x][y] = start_num


if __name__ == "__main__":
    play_game()
