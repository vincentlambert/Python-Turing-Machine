import pytest

from turing_machine import TuringMachine


def test_init_no_config_file():
    with pytest.raises(ValueError) as e_info:
        tm = TuringMachine()


def test_init():
    tm = TuringMachine("config/test.json")
    assert tm.state == "e1"
