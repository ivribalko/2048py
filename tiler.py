import random
from config import row_count, col_count
from direction import Direction
from tile import Tile


class SameTileError(Exception):
    pass


class NoEmptyTileError(Exception):
    pass


def try_move_tile_into(move_from, move_to):
    if move_to == move_from:
        raise SameTileError("Moving from and to are same")

    if move_to.is_empty() or move_to.value == move_from.value:
        move_to.value += move_from.value
        move_from.value = 0
        return True
    return False


class Tiler:
    __tiles = [[Tile() for y in range(row_count)] for x in range(col_count)]
    __random_indexes = list(range(col_count))

    def apply_move(self, direction):
        if direction is Direction.UP:
            self.apply_move_vertical(from_max_to_min=False)
        if direction is Direction.DOWN:
            self.apply_move_vertical(from_max_to_min=True)
        if direction is Direction.LEFT:
            self.apply_move_horizontal(from_max_to_min=False)
        if direction is Direction.RIGHT:
            self.apply_move_horizontal(from_max_to_min=True)

    def apply_move_vertical(self, from_max_to_min):
        max_index = row_count - 1
        for x in range(col_count):
            move_next_into = max_index if from_max_to_min else 0
            if from_max_to_min:
                vertical_range = reversed(range(max_index))
            else:
                vertical_range = range(1, max_index + 1)

            for y in vertical_range:
                moving_tile = self.__tiles[x][y]

                if moving_tile.is_empty():
                    continue

                if not try_move_tile_into(moving_tile, self.__tiles[x][move_next_into]):
                    empty_y = move_next_into + -1 if from_max_to_min else 1
                    try:
                        try_move_tile_into(moving_tile, self.__tiles[x][empty_y])
                        move_next_into = empty_y
                    except SameTileError:
                        move_next_into = y

    def apply_move_horizontal(self, from_max_to_min):
        pass

    def get_row_text(self, row_index):
        row_text = ''
        for x in range(col_count):
            row_text += self.__tiles[x][row_index].get_text()
        return row_text

    def clear(self):
        for x in range(row_count):
            for y in range(col_count):
                self.__tiles[x][y].value = 0

    def spawn_new(self):
        empty = self.get_random_empty()
        empty.value = 2

    def get_random_empty(self):
        random.shuffle(self.__random_indexes)
        for x in self.__random_indexes:
            for y in self.__random_indexes:
                random_tile = self.__tiles[x][y]
                if random_tile.is_empty():
                    return random_tile

        raise NoEmptyTileError("No empty tile")
