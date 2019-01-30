import random
from tile import Tile

class Tiler:
  tiles = []
  row_count = 0
  col_count = 0
  random_indexes = []

  def __init__(self, row_count, col_count):
    if row_count != col_count:
      raise Exception('Same row and col expected')

    self.tiles = [[Tile() for x in range(col_count)] for y in range(row_count)]
    self.row_count = row_count
    self.col_count = col_count
    self.random_indexes = list(range(col_count))

  def get_row_text(self, row_index):
    row_text = ''
    for x in range(self.col_count):
      row_text += self.tiles[row_index][x].get_text()
    return row_text

  def clear(self):
    for x in range(self.row_count):
      for y in range(self.col_count):
        self.tiles[x][y].value = 0

  def spawn_new(self):
    empty = get_random_empty()

  def get_random_empty(self):
    random.shuffle(self.random_indexes)
    for x in self.random_indexes:
      for y in self.random_indexes:
        random_tile = self.tiles[x][y]
        if random_tile.is_empty():
          return random_tile

    raise Exception("No empty tile")