""" 
This file contains the status of the Tic Tac Toe - board
"""
from users import Users
from enum import Enum, auto
from dataclasses import dataclass


class Cellstate(
    Enum
):  # Do not use @dataclass cause Enum inherit its own __str__ method
    """Cell states class to choice between circle, cross or blank as attributs"""

    blank = auto()  # value = 1
    circle = auto()  # value = 2
    cross = auto()  # value = 3


@dataclass
class Cellstatus:
    """Cell status class to set or get their status"""

    status: Cellstate

    def __init__(self):
        """Initialize cellstatus for blank by default"""
        self.status = Cellstate.blank

    def get_status(self):
        """Method to get the name of last saved cell status"""
        return self.status.name

    def set_status(self, state: int) -> None:
        """Method to set blank(1), circle(2) or cross(3) state"""
        match state:
            case Cellstate.blank.value:
                self.status = Cellstate.blank
            case Cellstate.circle.value:
                self.status = Cellstate.circle
            case Cellstate.cross.value:
                self.status = Cellstate.cross


# c1 = Cellstatus
# print(c1.get_status())
# c1.set_status(2)
# print(c1.get_status())
# c1.set_status(3)
# print(c1.get_status())


@dataclass
class Row:
    """Row class to define the status of its three cells"""

    cell1: Cellstatus
    cell2: Cellstatus
    cell3: Cellstatus

    def __init__(self):
        """Define a cellstatus object for each cell in a new row"""
        self.cell1 = Cellstatus()
        self.cell2 = Cellstatus()
        self.cell3 = Cellstatus()

    def __str__(self) -> str:
        return f"{self.cell1.get_status()} | {self.cell2.get_status()} | {self.cell3.get_status()}"

    def set_row_status(self, column: int, state: int) -> None:
        """Method to change a given cell in column 1-3 for blank(1), circle(2) or cross(3) state"""
        match column:
            case 1:
                self.cell1.set_status(state)
                print(self)
            case 2:
                self.cell2.set_status(state)
                print(self)
            case 3:
                self.cell3.set_status(state)
                print(self)
            case _:
                print(
                    "Invalid case. Choose an available state: blank(1), circle(2) or cross(3) "
                )


# r1 = Row()
# print(r1)
# print(repr(r1))
# r1.set_row_status(1, 2)
# r1.set_row_status(2, 3)
# r1.set_row_status(3, 2)


@dataclass
class Board:
    """Board class to set the status of their three rows"""

    row1: Row
    row2: Row
    row3: Row
    users: Users
    gameid: int

    def __init__(self, users: Users, gameid: int):
        self.row1 = Row()
        self.row2 = Row()
        self.row3 = Row()
        self.users = users
        self.gameid = gameid

    def __str__(self) -> str:
        """Print fonction of Board Class"""
        return f"{self.gameid} status:\n{self.row1} \n{self.row2} \n{self.row1}"


# u=Users()
# u.new("User1", 1, 1)
# u.new("User2", 1, 1)

# b = Board(u, 1)
# print(b)
