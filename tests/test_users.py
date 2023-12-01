from OXO.users import Users, User


def test_new_user():
    users = Users()
    users.new("User1", 1, 1)
    print(users.usersList)
    assert users.usersList == [User(1, "User1", 1, 1)]


def test_new_users_list():
    users = Users()
    users.new("User1", 1)  # Must assing a None gameid
    users.new("User2", 1, 0)
    users.new("User3", 1, 0)
    assert users.usersList == [
        User(1, "User1", 1, None),
        User(2, "User2", 1, 0),
        User(3, "User3", 1, 0),
    ]


def test_gameid_assignement() -> None:
    users = Users()
    users.new("User1", 1)  # Must assing a None gameid
    users.new("User2", 1)
    users.new("User3", 1)

    users.set_gameid(2, 241)
    assert users.usersList == [
        User(1, "User1", 1, None),
        User(2, "User2", 1, 241),
        User(3, "User3", 1, None),
    ]
