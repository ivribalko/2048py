from config import row_count
from drawer import row, clear
from tiler import Tiler, NoEmptyTileError
from direction import Direction

keyboard_to_direction = {
    'w': Direction.UP,
    'a': Direction.LEFT,
    's': Direction.DOWN,
    'd': Direction.RIGHT,
}


def spawn_new_and_redraw():
    tiler.spawn_new()
    clear()
    for x in range(row_count):
        row(tiler.get_row_text(x))


tiler = Tiler()
spawn_new_and_redraw()

while True:
    try:
        direction = keyboard_to_direction[input()]
        tiler.apply_move(direction)
        spawn_new_and_redraw()
    except KeyError as e:
        if str(e) == 'q':
            break
        elif str(e) == 'r':
            tiler.clear()
        else:
            print("Use W/A/S/D, R, Q")
    except NoEmptyTileError:
        tiler.clear()
        spawn_new_and_redraw()
