""" 
This file contains the user class and the userslist
"""
from typing import (
    TypeAlias,
    Optional,
)  # "from typing_extensions" in Python 3.9 and earlier

IdType: TypeAlias = int  # declare a type alias that coud be changed easily


class User:
    """User Class to register nickname, image and game id"""

    userid: IdType
    nickname: str
    image: int
    gameid: Optional[int]

    def __init__(
        self,
        userid: IdType,
        nickname: str,
        image: int,
        gameid: Optional[IdType],
    ):
        self.userid = userid
        self.nickname = nickname
        self.image = image
        self.gameid = gameid

    def __str__(self):
        """Print user's settings"""
        return f"({self.nickname}) {self.image} {self.gameid})"

    def __repr__(self):
        return str(self)

    def __eq__(self, otherUser: object) -> bool:
        if isinstance(otherUser, User):
            return (
                (self.userid == otherUser.userid)
                and (self.nickname == otherUser.nickname)
                and (self.image == otherUser.image)
                and (self.gameid == otherUser.gameid)
            )
        return False


class Users:
    """List of registered users"""

    usersList: list[User]

    def __init__(self):
        self.usersList = []

    def __str__(self):
        return str(self.usersList)

    def __repr__(self):
        return str(self)

    def new(
        self, nickname: str, image: int, gameid: Optional[IdType] = None
    ) -> User:
        """Method to register users objects type (nickname, image, game id) in users' list"""
        userid = (
            len(self.usersList) + 1
        )  # TODO: search for userid libraries "uuid"
        user = User(userid, nickname, image, gameid)
        self.usersList.append(user)

        return user

    def set_gameid(self, userid: IdType, gameid: IdType):
        """Method to asign a gameid to existent user"""
        for user in self.usersList:
            if user.userid == userid:
                user.gameid = gameid
        return "User not found"
