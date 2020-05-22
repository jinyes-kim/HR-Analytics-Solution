import sqlite3


class User:
    def __init__(self, id, power):
        self.id = id
        self.power = power


def connect_db():
    con = sqlite3.connect("C:/calcul/data/user.db")
    sqlite3.Connection
    cursor = con.cursor()
    cursor.execute("SELECT id, pwd, power FROM users")
    db = tmp = cursor.fetchall()
    user_dict = {}
    for a in tmp:
        user_dict[a[0]] = a[:]
    return user_dict


def login(user_dict, id, pw):
    if user_dict[id][1] == pw:
        return True
    return False


def view_init():
    print("┌────────────────────────────────────────┐ ")
    print("│  Ready to Start                        │ ")
    print("│                    Enter Any key       │ ")
    print("└────────────────────────────────────────┘ ")


def view_load():
    print("┌────────────────────────────────────────┐ ")
    print("│           Data Loading...              │ ")
    print("└────────────────────────────────────────┘ ")

def view_start():
    print("┌────────────────────────────────────────┐ ")
    print("│           Management System            │ ")
    print("└────────────────────────────────────────┘ ")

def view_login(id):
    print("┌────────────────────────────────────────┐ ")
    print("  {} 님 환영합니다            ".format(id))
    print("└────────────────────────────────────────┘ ")

def clear_screen():
    for _ in range(30):
        print()

