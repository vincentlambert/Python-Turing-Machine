from turing_machine import Tape


def test_instanciate_tape():
    tape = Tape()
    assert tape is not None


def test_read_write_empty_tape():
    tape = Tape()
    assert tape.read() == None
    tape.write("a")
    assert tape.read() == "a"


def test_move_read_write():
    tape = Tape()

    tape.write("a")
    assert tape.read() == "a"

    tape.move_right()
    assert tape.read() == None

    tape.write("b")
    assert tape.read() == "b"

    tape.move_left()
    assert tape.read() == "a"


def test_extend_to_left():
    tape = Tape()

    tape.write("a")
    assert tape.read() == "a"

    tape.move_left()
    assert tape.read() == None

    tape.write("b")
    assert tape.read() == "b"

    tape.move_left()
    assert tape.read() == None

    tape.move_right()
    tape.move_right()
    assert tape.read() == "a"


def test_load_memory():
    memory = ["a", "b"]
    tape = Tape(memory=memory)
    assert tape.read() == "a"
    tape.move_right()
    assert tape.read() == "b"
    tape.move_right()
    assert tape.read() == None
    tape.move_left()
    assert tape.read() == "b"
    tape.move_left()
    assert tape.read() == "a"
    tape.move_left()
    assert tape.read() == None


def test_blank_symbol():
    tape = Tape(blank_symbol=" ")
    assert tape.read() == " "
    tape.write("a")
    assert tape.read() == "a"
    tape.move_right()
    assert tape.read() == " "
    tape.move_left()
    assert tape.read() == "a"
    tape.move_left()
    assert tape.read() == " "
    tape.move_right()
    assert tape.read() == "a"
    tape.move_right()
    assert tape.read() == " "


def test_reset():
    tape = Tape(["a", "b"])
    tape.write("c")
    assert tape.read() == "c"
    tape.move_right()
    assert tape.read() == "b"
    tape.reset()
    assert tape.read() == "a"
    tape.move_right()
    assert tape.read() == "b"
