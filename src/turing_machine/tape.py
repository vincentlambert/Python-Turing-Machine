class Tape:

    def __init__(self, memory: list = None, blank_symbol: object = None) -> None:
        self._position = 0
        self._blank_symbol = blank_symbol
        self._init_data = memory
        self.reset()

    def reset(self) -> None:
        self._position = 0
        if self._init_data is None:
            self._data = [self._blank_symbol]
        else:
            self._data = self._init_data.copy()

    def read(self) -> object:
        return self._data[self._position]

    def write(self, value) -> None:
        self._data[self._position] = value

    def move_left(self) -> None:
        if self._position == 0:
            self._data.insert(0, self._blank_symbol)
        else:
            self._position -= 1

    def move_right(self) -> None:
        self._position += 1
        if self._position == len(self._data):
            self._data.append(self._blank_symbol)
