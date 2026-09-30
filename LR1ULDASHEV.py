import time
import os

RED = '\u001b[41m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'


def flag():
    pixel = ' '
    height = 10

    for i in range(height):
        if i < 2 or i > 7:
            print(RED + pixel * 20 + RESET)
        elif i == 4 or i == 5:
            print(RED + pixel * 4 + WHITE + pixel * 12 + RED + pixel * 4 + RESET)
        else:
            print(RED + pixel * 8 + WHITE + pixel * 4 + RED + pixel * 8 + RESET)


def pattern():
    line1 = "  **    **    "
    line2 = " *  *  *  *   "
    line3 = " *  *  *  *   "
    line4 = "  **    **    "

    for i in range(2):
        print(line1 * 4)
        print(line2 * 4)
        print(line3 * 4)
        print(line4 * 4)


def animation():
    for i in range(1, 5):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\u001b[{i * 2};{i * 4}H' + RED + f' Frame {i} ' + RESET)
        time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')


def sequence():
    file = open('sequence.txt', 'r')
    in_range = []
    out_range = []

    for line in file:
        val = float(line)
        if val >= -3 and val <= 3:
            in_range.append(val)
        else:
            out_range.append(val)

    file.close()

    total = len(in_range) + len(out_range)

    perc_in = len(in_range) / total * 100
    perc_out = len(out_range) / total * 100

    # Отрисовка полос по формуле (длина списка / 5)
    print(f'{RED}{" " * int(len(in_range) / 5)}{RESET} {perc_in}%')
    print(f'{WHITE}{" " * int(len(out_range) / 5)}{RESET} {perc_out}%')


flag()
pattern()
animation()
sequence()
