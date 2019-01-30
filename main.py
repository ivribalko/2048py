
from drawer import Drawer
from enum import Enum
from tile import Tile
from tiler import Tiler

row_count = 4
col_count = 4

tiler = Tiler(row_count, col_count)
drawer = Drawer()

empty = tiler.get_random_empty()
empty.value = 2
empty = tiler.get_random_empty()
empty.value = 2
empty = tiler.get_random_empty()
empty.value = 2

print(input())

drawer.clear()

for x in range(row_count):
  drawer.row(tiler.get_row_text(x))