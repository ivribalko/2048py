from config import tile_width


class Tile:
    value = 0

    def __init__(self):
        self.__empty_text = f'|{" " * tile_width}|'
        self.__format_text = f'|{{:0{tile_width}d}}|'

    def is_empty(self):
        return self.value == 0

    def get_text(self):
        if self.value == 0:
            return self.__empty_text
        return self.__format_text.format(self.value)
