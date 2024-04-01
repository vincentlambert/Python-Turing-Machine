import pytest

from turing_machine import TuringMachine


@pytest.fixture
def basic_config_dict():
    return {
        "initial_state": "e1",
        "tape": {"blank_symbol": 0},
        "program": [
            {
                "state": "e1",
                "inputs": [
                    {"input": 1, "write": 0, "move": "R", "next_state": "e2"},
                    {"input": 0},
                ],
            },
            {
                "state": "e2",
                "inputs": [
                    {"input": 1, "write": 0, "move": "R", "next_state": "e1"},
                    {"input": 0},
                ],
            },
        ],
    }


def test_init_no_config():
    with pytest.raises(ValueError) as e_info:
        tm = TuringMachine()


def test_init_config_conflic():
    with pytest.raises(ValueError) as e_info:
        tm = TuringMachine(config_dict={}, config_file="config/test.json")


def test_init_from_file():
    tm = TuringMachine(config_file="config/test.json")
    assert tm.state == "e1"


def test_init_from_dict():
    tm = TuringMachine(config_dict={"initial_state": "e1"})
    assert tm.state == "e1"


def test_reset():
    tm = TuringMachine(config_dict={"initial_state": "e1"})
    tm._current_state = "X"
    tm.reset()
    assert tm.state == "e1"
    tm.reset(["a", "b"])
    assert tm.tape.read() == "a"


def test_init_from_dict(basic_config_dict):
    tm = TuringMachine(config_dict=basic_config_dict)
    assert tm.state == "e1"
    assert tm.tape.data == [0]
    assert tm.tape.blank_symbol == 0
    assert tm._transitions["e1#1"].next_state == "e2"
    assert tm._transitions["e1#1"].write == 0
    assert tm._transitions["e1#1"].move == "R"
    assert tm._transitions["e1#0"].next_state is None
    assert tm._transitions["e1#0"].write is None
    assert tm._transitions["e1#0"].move is None
    assert tm._transitions["e2#1"].next_state == "e1"
    assert tm._transitions["e2#1"].write == 0
    assert tm._transitions["e2#1"].move == "R"
    assert tm._transitions["e2#0"].next_state is None
    assert tm._transitions["e2#0"].write is None
    assert tm._transitions["e2#0"].move is None


def test_simple_program_step_one(basic_config_dict):
    tm = TuringMachine(config_dict=basic_config_dict)
    tm.reset([1, 1])
    assert tm.state == "e1"
    assert tm.tape.read() == 1
    tm.run(steps=1)
    assert tm.state == "e2"
    assert tm.tape.read() == 1
    tm.run(steps=1)
    assert tm.state == "e1"
    assert tm.tape.read() == 0
    tm.run(steps=1)
    assert tm.state == None
    assert tm.memory == [0, 0, 0]


def test_simple_program_step_loop(basic_config_dict):
    tm = TuringMachine(config_dict=basic_config_dict)
    tm.reset([1, 1, 1])
    tm.run(steps=2)
    assert tm.state == "e1"
    assert tm.memory == [0, 0, 1]


def test_simple_program_step_full(basic_config_dict):
    tm = TuringMachine(config_dict=basic_config_dict)
    tm.reset([1, 1, 1, 1])
    tm.run(steps=-1)
    assert tm.state == None
    assert tm.memory == [0, 0, 0, 0, 0]
