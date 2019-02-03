import random
from direction import Direction
from tile import Tile


def try_move_tile_into(move_from, move_to):
    if move_to == move_from:
        raise Exception("Moving from and to are same")

    if move_to.is_empty() or move_to.value == move_from.value:
        move_to.value += move_from.value
        move_from.value = 0
        return True
    return False


class Tiler:
    tiles = []
    row_count = 0
    col_count = 0
    random_indexes = []

    def __init__(self, row_count, col_count):
        self.tiles = [[Tile() for y in range(row_count)] for x in range(col_count)]
        self.row_count = row_count
        self.col_count = col_count
        self.random_indexes = list(range(col_count))

    def apply_move(self, direction):
        if direction is Direction.DOWN:
            max_y = self.row_count - 1
            for x in range(0, self.col_count):
                last_busy_y = max_y
                for y in reversed(range(0, max_y)):
                    moving_tile = self.tiles[x][y]

                    if moving_tile.is_empty():
                        continue

                    if not try_move_tile_into(moving_tile, self.tiles[x][last_busy_y]):
                        empty_y = last_busy_y - 1
                        if empty_y != y and empty_y >= 0:
                            try_move_tile_into(moving_tile, self.tiles[x][empty_y])
                            last_busy_y = empty_y
                        else:
                            last_busy_y = y


    def get_row_text(self, row_index):
        row_text = ''
        for x in range(self.col_count):
            row_text += self.tiles[x][row_index].get_text()
        return row_text

    def clear(self):
        for x in range(self.row_count):
            for y in range(self.col_count):
                self.tiles[x][y].value = 0

    def spawn_new(self):
        empty = self.get_random_empty()
        empty.value = 2

    def get_random_empty(self):
        random.shuffle(self.random_indexes)
        for x in self.random_indexes:
            for y in self.random_indexes:
                random_tile = self.tiles[x][y]
                if random_tile.is_empty():
                    return random_tile

        raise Exception("No empty tile")
