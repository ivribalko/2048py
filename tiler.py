import random
from config import row_count, col_count, new_tile_values
from direction import Direction
from tile import Tile


class SameTileError(Exception):
    pass


class NoEmptyTileError(Exception):
    pass


class Tiler:
    __random_indexes_x = list(range(col_count))
    __random_indexes_y = list(range(row_count))

    def __init__(self):
        tiles = [[Tile() for y in range(row_count)] for x in range(col_count)]
        self.__rows = []
        for y in range(row_count):
            row = []
            for x in range(col_count):
                row.append(tiles[x][y])
            self.__rows.append(row)
        self.__cols = []
        for x in range(col_count):
            col = []
            for y in range(row_count):
                col.append(tiles[x][y])
            self.__cols.append(col)

    def apply_move(self, direction):
        if direction is Direction.UP:
            self.apply_move_for_tiles(self.__cols, _reversed=False)
        if direction is Direction.DOWN:
            self.apply_move_for_tiles(self.__cols, _reversed=True)
        if direction is Direction.LEFT:
            self.apply_move_for_tiles(self.__rows, _reversed=False)
        if direction is Direction.RIGHT:
            self.apply_move_for_tiles(self.__rows, _reversed=True)

    @staticmethod
    def apply_move_for_tiles(tiles, _reversed):
        for _list in tiles:
            move_next_into = len(_list) - 1 if _reversed else 0
            if _reversed:
                _range = reversed(range(len(_list) - 1))
            else:
                _range = range(1, len(_list))
            for index in _range:
                moving_tile = _list[index]
                if moving_tile.is_empty():
                    continue

                if not Tiler.try_move_tile_into(moving_tile, _list[move_next_into]):
                    empty_y = move_next_into + (-1 if _reversed else 1)
                    try:
                        Tiler.try_move_tile_into(moving_tile, _list[empty_y])
                        move_next_into = empty_y
                    except SameTileError:
                        move_next_into = index

    @staticmethod
    def try_move_tile_into(move_from, move_to):
        if move_from == move_to:
            raise SameTileError("Moving from and to are same")

        if move_to.is_empty() or move_to.value == move_from.value:
            move_to.value += move_from.value
            move_from.value = 0
            return True
        return False

    def get_row_text(self, row_index):
        row_text = ''
        for tile in self.__rows[row_index]:
            row_text += tile.get_text()
        return row_text

    def clear(self):
        for row in self.__rows:
            for tile in row:
                tile.value = 0

    def spawn_new_tile(self):
        empty = self.get_random_empty_tile()
        empty.value = random.choice(new_tile_values)

    def get_random_empty_tile(self):
        random.shuffle(self.__random_indexes_x)
        random.shuffle(self.__random_indexes_y)
        for x in self.__random_indexes_x:
            row = self.__rows[x]
            for y in self.__random_indexes_y:
                random_tile = row[y]
                if random_tile.is_empty():
                    return random_tile

        raise NoEmptyTileError("No empty tile")
