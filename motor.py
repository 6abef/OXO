""" 
This file registrer the status of a Tic Tac Toe- board"""
from users import Users 
import enum



class Cellstatus(enum):
    """Cell' status  Class to choice wheather cercle, cross or blank"""
    def _init_(self):
        self.cercle = enum.auto()
        self.cross = enum.auto()
        self.blank = enum.auto()

class Row:
    """Row Class to define theirs status"""
    def _init_(self):
        self.column1 = Cellstatus
        self.column2 = Cellstatus
        self.column3 = Cellstatus 
    
    
class Board:
    """ Board Class"""
    def __init__(self, cells: dict(), status: [[str],[str]], users:Users, gameid:int ):
        self.cells = dict( A1=None, A2=None, A3=None, B1=None, B2=None, B3=None, C1=None, C2=None, C3=None)
        self.status = status
        self.users = users
        self.gameid =gameid
    
    def __str__(self):
        """Print fonction of Board Class"""
        return f"( {self.gameid}) status |  Celdas disponibles: {self.status[0]}, Celdas ocupadas {self.status[1]})"