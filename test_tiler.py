import unittest
from config import row_count, col_count
from direction import Direction
from tiler import Tiler


class TilerUnitTest(unittest.TestCase):
    def setUp(self):
        self.tiler = Tiler()
        self.assertEqual(row_count, 4, "Not ready for other table configuration")
        self.assertEqual(col_count, 4, "Not ready for other table configuration")

    def test_move_result_when_column_2222(self):
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 2, 2, 2],
            expected=[0, 0, 4, 4])

    def test_move_result_when_column_2248(self):
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 2, 8, 16],
            expected=[0, 4, 8, 16])

    def test_move_result_when_column_24816(self):
        self.assert_move_result_column(
            direction=Direction.DOWN,
            values=[2, 4, 8, 16],
            expected=[2, 4, 8, 16])

    def test_move_result_when_row_4082(self):
        self.assert_move_result_row(
            direction=Direction.LEFT,
            values=[4, 0, 8, 2],
            expected=[4, 8, 2, 0])

    def test_move_result_when_row_4082_2(self):
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



