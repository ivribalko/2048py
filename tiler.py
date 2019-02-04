import random
import config
from direction import Direction
from tile import Tile


class Tiler:
    __random_indexes_x = list(range(config.col_count))
    __random_indexes_y = list(range(config.row_count))

    def __init__(self):
        tiles = [[Tile() for y in range(config.row_count)] for x in range(config.col_count)]
        self.__rows = []
        for y in range(config.row_count):
            row = []
            for x in range(config.col_count):
                row.append(tiles[x][y])
            self.__rows.append(row)
        self.__cols = []
        for x in range(config.col_count):
            col = []
            for y in range(config.row_count):
                col.append(tiles[x][y])
            self.__cols.append(col)
        self.__stub_tile_row_text_top = f'|{"¯" * config.tile_width}|' * config.col_count + '\n'
        self.__stub_tile_row_text_bot = '\n' + f'|{"_" * config.tile_width}|' * config.col_count

    def apply_move(self, direction: Direction):
        if direction is Direction.UP:
            self.apply_move_for_tiles(self.__cols, _reversed=False)
        if direction is Direction.DOWN:
            self.apply_move_for_tiles(self.__cols, _reversed=True)
        if direction is Direction.LEFT:
            self.apply_move_for_tiles(self.__rows, _reversed=False)
        if direction is Direction.RIGHT:
            self.apply_move_for_tiles(self.__rows, _reversed=True)

    @staticmethod
    def apply_move_for_tiles(tiles: list, _reversed: bool):
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
    def try_move_tile_into(move_from: Tile, move_to: Tile) -> bool:
        if move_from == move_to:
            raise SameTileError("Moving from and to are same")

        if move_to.is_empty() or move_to.value == move_from.value:
            move_to.value += move_from.value
            move_from.value = 0
            return True
        return False

    def get_row_text(self, row_index: int) -> str:
        row_text = self.__stub_tile_row_text_top
        for tile in self.__rows[row_index]:
            row_text += tile.get_text()
        row_text += self.__stub_tile_row_text_bot
        return row_text

    def clear(self):
        for row in self.__rows:
            for tile in row:
                tile.value = 0

    def spawn_new_tile(self):
        empty = self.get_next_empty_tile()
        empty.value = random.choice(config.new_tile_values)

    def get_next_empty_tile(self) -> Tile:
        for x in self.__random_indexes_x:
            column = self.__cols[x]
            for y in self.__random_indexes_y:
                result = column[y]
                if result.is_empty():
                    return result

    def get_random_empty_tile(self) -> Tile:
        random.shuffle(self.__random_indexes_x)
        random.shuffle(self.__random_indexes_y)
        for x in self.__random_indexes_x:
            column = self.__cols[x]
            for y in self.__random_indexes_y:
                result = column[y]
                if result.is_empty():
                    return result

        raise NoEmptyTileError("No empty tile")


class SameTileError(Exception):
    pass


class NoEmptyTileError(Exception):
    pass
