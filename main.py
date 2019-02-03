from config import row_count
from drawer import row, clear_screen
from tiler import Tiler, NoEmptyTileError
from direction import keyboard_to_direction


def spawn_new_and_redraw():
    tiler.spawn_new_tile()
    clear_screen()
    for x in range(row_count):
        row(tiler.get_row_text(x))


def restart():
    tiler.clear()
    spawn_new_and_redraw()


tiler = Tiler()
restart()

while True:
    try:
        direction = keyboard_to_direction[input()]
        tiler.apply_move(direction)
        spawn_new_and_redraw()
    except KeyError as e:
        if str(e) == '\'q\'':
            break
        elif str(e) == '\'r\'':
            restart()
        else:
            print("Use W/A/S/D, R, Q")
    except NoEmptyTileError:
        restart()
