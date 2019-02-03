import unittest
import config
from direction import Direction
from tiler import Tiler


def force_table_resolution(cols, rows):
    def wrap(f):
        def wrapped_f(*args):
            config.col_count = cols
            config.row_count = rows
            f(*args, Tiler())
        return wrapped_f
    return wrap


class TilerUnitTest(unittest.TestCase):
    def setUp(self):
        self.col_count_save = config.col_count
        self.row_count_save = config.row_count

    def tearDown(self):
        config.col_count = self.col_count_save
        config.row_count = self.row_count_save

    @force_table_resolution(cols=3, rows=5)
    def test_move_up_for3x5(self, tiler):
        self.tiler = tiler
        self.set_column(0, [0, 0, 4])
        self.set_column(2, [0, 0, 0, 0, 2])
        self.tiler.apply_move(Direction.UP)

    @force_table_resolution(cols=4, rows=4)
    def test_move_result_when_column_2222(self, tiler):
        self.tiler = tiler
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 2, 2, 2],
            expected=[0, 0, 4, 4])

    @force_table_resolution(cols=4, rows=4)
    def test_move_result_when_column_2248(self, tiler):
        self.tiler = tiler
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 2, 8, 16],
            expected=[0, 4, 8, 16])

    @force_table_resolution(cols=4, rows=4)
    def test_move_result_when_column_24816(self, tiler):
        self.tiler = tiler
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 4, 8, 16],
            expected=[2, 4, 8, 16])

    @force_table_resolution(cols=4, rows=4)
    def test_move_result_when_row_4082(self, tiler):
        self.tiler = tiler
        self.assert_move_result_row(
            direction=Direction.LEFT,
            values=[4, 0, 8, 2],
            expected=[4, 8, 2, 0])

    @force_table_resolution(cols=4, rows=4)
    def test_move_result_when_row_4082_2(self, tiler):
        self.tiler = tiler
        self.assert_move_result_row(
            direction=Direction.RIGHT,
            values=[4, 0, 8, 2],
            expected=[0, 4, 8, 2])

    def assert_move_result_column(self, direction, values, expected):
        self.set_column(index=0, values=values)
        self.tiler.apply_move(direction)
        actual = self.get_values(self.tiler._Tiler__cols[0])
        self.assertSequenceEqual(expected, actual)

    def assert_move_result_row(self, direction, values, expected):
        self.set_row(index=0, values=values)
        self.tiler.apply_move(direction)
        actual = self.get_values(self.tiler._Tiler__rows[0])
        self.assertSequenceEqual(expected, actual)

    def set_column(self, index, values):
        column = self.tiler._Tiler__cols[index]
        for index, tile in enumerate(column):
            tile.value = values[index]

    def set_row(self, index, values):
        row = self.tiler._Tiler__rows[index]
        for index, tile in enumerate(row):
            tile.value = values[index]

    @staticmethod
    def get_values(tiles):
        result = []
        for tile in tiles:
            result.append(tile.value)
        return result



