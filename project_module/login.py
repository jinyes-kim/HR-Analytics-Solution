import sqlite3


def connect_db():
    con = sqlite3.connect("C:/calcul/data/user.db")
    sqlite3.Connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    db = tmp = cursor.fetchall()
    user_dict = {}
    for a in tmp:
        user_dict[a[0]] = a[:]
    return user_dict


def login(user_dict, id, pw):
    try:
        if user_dict[id][1] == pw:
            return True
    except:
        return False
    return False
