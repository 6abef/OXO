""" 
This file contains the user class and the userslist
"""


class User:
    """User Class to register nickname, image and game id"""

    def __init__(self, userid, nickname: str, image: int, gameid: int):
        self.userid = userid
        self.nickname = nickname
        self.image = image
        self.gameid = gameid

    def __str__(self):
        """Print user's settings"""
        return f"({self.nickname}) {self.imagen} {self.gameid})"


class Users:
    """List of registered users"""

    lista: list[User] = []

    def new(self, nickname: str, image: int, gameid) -> User:
        """Method to register users objects type (nickname, image, game id) in users' list"""
        userid = len(self.lista) + 1
        user = User(userid, nickname, image, gameid)
        Users.lista.append(user)
        return user
