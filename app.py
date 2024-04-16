from __future__ import annotations
from abc import ABC, abstractmethod


# Context class
class VendingMachine:
    def __init__(self, initial_state: State) -> None:
        self._state: State = initial_state

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        print(f"Changing state to {type(state).__name__}")
        self._state = state

    def insert_money(self, amount: int) -> None:
        self._state.insert_money(self, amount)

    def make_selection(self) -> None:
        self._state.make_selection(self)

    def dispense_item(self) -> None:
        self._state.dispense_item(self)

    def return_money(self) -> None:
        self._state.return_money(self)


# State interface
class State(ABC):
    @abstractmethod
    def insert_money(self, vending_machine: VendingMachine, amount: int) -> None:
        pass

    @abstractmethod
    def make_selection(self, vending_machine: VendingMachine) -> None:
        pass

    @abstractmethod
    def dispense_item(self, vending_machine: VendingMachine) -> None:
        pass

    @abstractmethod
    def return_money(self, vending_machine: VendingMachine) -> None:
        pass


# Concrete states
class HasMoneyState(State):
    def insert_money(self, vending_machine: VendingMachine, amount: int) -> None:
        print("You have already inserted money.")

    def make_selection(self, vending_machine: VendingMachine) -> None:
        print("Selecting item...")
        vending_machine.state = SoldState()

    def dispense_item(self, vending_machine: VendingMachine) -> None:
        print("Cannot dispense item yet. Please make a selection first.")

    def return_money(self, vending_machine: VendingMachine) -> None:
        print("Returning money...")
        vending_machine.state = NoMoneyState()


class NoMoneyState(State):
    def insert_money(self, vending_machine: VendingMachine, amount: int) -> None:
        print(f"Inserted {amount} cents.")
        vending_machine.state = HasMoneyState()

    def make_selection(self, vending_machine: VendingMachine) -> None:
        print("Please insert money first.")

    def dispense_item(self, vending_machine: VendingMachine) -> None:
        print("Please insert money and make a selection first.")

    def return_money(self, vending_machine: VendingMachine) -> None:
        print("No money to return.")


class SoldState(State):
    def insert_money(self, vending_machine: VendingMachine, amount: int) -> None:
        print("Already dispensing an item. Please wait.")

    def make_selection(self, vending_machine: VendingMachine) -> None:
        print("Already dispensing an item. Please wait.")

    def dispense_item(self, vending_machine: VendingMachine) -> None:
        print("Dispensing item...")
        vending_machine.state = NoMoneyState()

    def return_money(self, vending_machine: VendingMachine) -> None:
        print("Already dispensing an item. Cannot return money.")


# Usage
if __name__ == "__main__":
    vending_machine = VendingMachine(NoMoneyState())

    vending_machine.insert_money(50)
    vending_machine.make_selection()
    vending_machine.dispense_item()

    vending_machine.insert_money(25)
    vending_machine.make_selection()
    vending_machine.dispense_item()

    vending_machine.return_money()
