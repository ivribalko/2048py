
from drawer import Drawer
from enum import Enum
from tile import Tile
from tiler import Tiler
from move_direction import MoveDirection

row_count = 4
col_count = 4

keyboard_to_direction = {
    'w': MoveDirection.UP,
    'a': MoveDirection.LEFT,
    's': MoveDirection.DOWN,
    'd': MoveDirection.RIGHT,
}

tiler = Tiler(row_count, col_count)
drawer = Drawer()

tiler.clear()

drawer.clear()

for x in range(row_count):
  drawer.row(tiler.get_row_text(x))

while True:
  try:
    direction = keyboard_to_direction[input()]
    print(direction)
  except KeyError as e:
    print("Use WASD")