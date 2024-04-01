import pytest
from turing_machine import Tape, Operation


@pytest.fixture
def empty_tape():
    return Tape()


def test_move_right_operation(empty_tape):
    operation = Operation(tape=empty_tape, write="a", move="R", next_state="s")
    next_state = operation.execute()
    assert next_state == "s"
    empty_tape.move_left()
    assert empty_tape.read() == "a"


def test_move_left_operation(empty_tape):
    operation = Operation(tape=empty_tape, write="a", move="L", next_state="s")
    next_state = operation.execute()
    assert next_state == "s"
    empty_tape.move_right()
    assert empty_tape.read() == "a"


def test_no_move_operation(empty_tape):
    operation = Operation(tape=empty_tape, write="a", next_state="s")
    next_state = operation.execute()
    assert next_state == "s"
    assert empty_tape.read() == "a"


def test_no_write_operation(empty_tape):
    empty_tape.write("a")
    operation = Operation(tape=empty_tape, next_state="s")
    next_state = operation.execute()
    assert next_state == "s"
    assert empty_tape.read() == "a"


def test_final_with_write(empty_tape):
    operation = Operation(tape=empty_tape, write="a")
    next_state = operation.execute()
    assert next_state == None
    assert empty_tape.read() == "a"


def test_final_without_write(empty_tape):
    operation = Operation(tape=empty_tape)
    next_state = operation.execute()
    assert next_state == None
    assert empty_tape.read() == None
