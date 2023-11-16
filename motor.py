""" 
This file saves the status of a Tic Tac Toe - board
"""
from users import Users 
from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class Cellstate(Enum): 
    """Cell states class to choice between cercle, cross or blank as attributs"""
    blank = auto()  # value = 1
    cercle = auto() # value = 2
    cross = auto()  # value = 3            
    
@dataclass
class Cellstatus: 
    """Cell status class to set or get their status"""
    status = Cellstate.blank
    
    @classmethod
    def get_status(self):
        """Method to get the name of last saved cell status"""
        return self.status.name
    
    @classmethod
    def set_status(self, state: int)-> None:
        """Method to set blank(1), cercle(2) or cross(3) state"""
        match state:
            case Cellstate.blank.value:
                self.status = Cellstate.blank
            case Cellstate.cercle.value:
                self.status = Cellstate.cercle
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
    """Row class to define the status of their three cells"""
    cell1 = Cellstatus
    cell2 = Cellstatus
    cell3 = Cellstatus 
      
    @classmethod   
    def display(self) -> str:
        return f"In this row: {self.cell1.get_status()} | {self.cell2.get_status()} | {self.cell3.get_status()}"
    
    @classmethod
    def set_row_status(self, colomn:int, state: int)-> None:
        """Method to change a given cell in colomn 1-3 for blank(1), cercle(2) or cross(3) state """
        match colomn:
            case 1:
                print("Cambiando celda en columna 1")
                self.cell1.set_status(state)
                print(f"{self.cell1.get_status()} {self.cell2.get_status()} {self.cell1.get_status()}")
            case 2:
                print("Cambiando celda en columna 2")
                self.cell2.set_status(state)
            case 3:
                print("Cambiando celda en columna 3")
                self.cell3.set_status(state)

r1 = Row
print(r1.display()) 
r1.set_row_status(1,2) # Why does all cells change its values?
    
@dataclass 
class Board:
    """ Board class to set the status of their three rows"""
    def __init__(self, users:Users, gameid:int) :
        self.row1 = Row 
        self.status = status
        self.users = users
        self.gameid =gameid
    
    def display(self)-> str:
        """Print fonction of Board Class"""
        return f"( {self.gameid}) status |  Celdas disponibles: {self.status[0]}, Celdas ocupadas {self.status[1]})"
    





