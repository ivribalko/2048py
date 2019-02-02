class Tile:
    value = 0

    def is_empty(self):
        return self.value == 0

    def get_text(self):
        if self.value == 0:
            return '[----]'
        return '[{:04d}]'.format(self.value)
