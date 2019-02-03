import unittest

from config import row_count
from direction import Direction
from tiler import Tiler


class TilerUnitTest(unittest.TestCase):
    def setUp(self):
        self.tiler = Tiler()

    def test_move_result_when_column_2222(self):
        self.assert_move_result_column(values=[2, 2, 2, 2], expected=[0, 0, 4, 4])

    def test_move_result_when_column_2248(self):
        self.assert_move_result_column(values=[2, 2, 8, 16], expected=[0, 4, 8, 16])

    def test_move_result_when_column_24816(self):
        self.assert_move_result_column(values=[2, 4, 8, 16], expected=[2, 4, 8, 16])

    def assert_move_result_column(self, values, expected):
        self.set_column(column_index=0, values=values)
        self.tiler.apply_move(Direction.DOWN)
        actual = self.get_column(0)
        self.assertSequenceEqual(expected, actual)

    def set_column(self, column_index, values):
        column = self.tiler._Tiler__tiles[column_index]
        for y in range(len(values)):
            column[y].value = values[y]

    def get_column(self, column_index):
        column = self.tiler._Tiler__tiles[column_index]
        result = []
        for y in range(row_count):
            result.append(column[y].value)
        return result



