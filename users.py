""" 
This file contains the user class and the userslist
"""

class User:
    """User Class to register nickname, image and game id """

    def __init__(self, nickname: str, image: int, gameid: int):
        self.nickname = nickname
        self.image = image
        self.gameid = int

    def __str__(self):
        """Print user's settings"""
        return f"({self.nickname}) {self.imagen} {self.gameid})"
    
class Users:
    """List of defined users"""
    lista:[User] = []
    
    @staticmethod
    def crear(nickname: str, image: int, gameid) -> User:
        """Method to register users objects type (nickname, image, game id) in users' list"""
        user = User(nickname, image, gameid)
        Users.lista.append(user)
        return user