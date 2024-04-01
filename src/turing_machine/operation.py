class Operation:
    def __init__(self, tape, write=None, move=None, next_state=None):
        self._tape = tape
        self._write = write
        self._move = move
        self._next_state = next_state

    @property
    def write(self) -> object:
        return self._write

    @property
    def move(self) -> object:
        return self._move

    @property
    def next_state(self) -> object:
        return self._next_state

    def execute(self) -> object:
        """Execute the operation on the tape.

        Returns:
            object: Returns the next state if it is not a final state, otherwise None.
        """
        if self._write is not None:
            self._tape.write(self._write)

        if self._move == "L":
            self._tape.move_left()
        elif self._move == "R":
            self._tape.move_right()

        if self._next_state is not None:
            return self._next_state

        return None
