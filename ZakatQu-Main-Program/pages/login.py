from getpass import getpass
from typing import List

from utils import terminal
from utils.db import login_query



def login() -> List[str] | str:
    terminal.clear_screen()

    print("Halaman Login\n")

    username: str = input("Username : ")
    password: str = getpass("Password : ")

    if username == "Takmir" and password == "Takmir" :
        return "Takmir"
    
    data: list[tuple] = login_query(username, password)

    return data