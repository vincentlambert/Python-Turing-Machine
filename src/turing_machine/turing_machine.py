import json

from .operation import Operation
from .tape import Tape


class TuringMachine:
    def __init__(self, config_file: str = None) -> None:
        if config_file is None:
            raise ValueError("No configuration file provided")
        self._load_config(config_file)

    def _load_config(self, config_file: str) -> dict:
        with open(config_file, "r") as f:
            config = json.load(f)

        #
        # Init tape
        #
        memory = None
        blank_symbol = None

        if config.get("tape", None) is not None:
            memory = config["tape"].get("initial_memory", None)
            blank_symbol = config["tape"].get("blank_symbol", None)

        self._tape = Tape(memory=memory, blank_symbol=blank_symbol)

        #
        # Init state
        #
        self.initial_state = config.get("initial_state", None)
        if self.initial_state is None:
            raise ValueError("No initial state provided")

        self._current_state = self.initial_state

        #
        # Init program
        #
        self._transitions = {}
        for operation in config.get("program", []):
            for input in operation.get("inputs", []):
                tag = f"{operation['state']}#{input['input']}"
                self._transitions[tag] = Operation(
                    tape=self._tape,
                    write=input.get("write", None),
                    move=input.get("move", None),
                    next_state=input.get("next_state", None),
                )

    @property
    def state(self) -> str:
        return self._current_state

    @property
    def memory(self) -> str:
        return self._tape._data

    def reset(self) -> None:
        self._current_state = self.initial_state
        self._tape.reset()

    def run(self, steps=1) -> None:
        """Execute the Turing Machine for a number of steps or stops if:
        - no more transitions are available
        - the current state is a final state
        - the currnet state is None

        If steps is not provided, the machine will run for 1 step.
        If steps is provided, the machine will run for that number of steps.
        If steps is 0, the machine will not run.
        If steps is negative, the machine will run indefinitely.

        Args:
            steps (int, optional): _description_. Defaults to 1.
        """
        if steps == 0:
            return

        while True:
            tag = f"{self._current_state}#{self._tape.read()}"
            if tag not in self._transitions:
                break

            new_state = self._transitions[tag].execute()
            if new_state is None:
                break

            self._current_state = new_state
            print(
                f"Move from: {self._current_state}\tto: {new_state}\twith: {self._tape._data}"
            )
            steps -= 1
            if steps == 0:
                break


if __name__ == "__main__":
    tm = TuringMachine("config/test.json")
    tm.run(15)
