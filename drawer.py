import os
from config import row_count


def draw_all(tiler):
    for x in range(row_count):
        print(tiler.get_row_text(x))


def clear_screen():
    os.system('clear')
