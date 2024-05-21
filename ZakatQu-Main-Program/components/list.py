from typing import List

def print_list(menus: List[str]):

    for idx, menu in enumerate(menus):
        print(f"{idx+1}. {menu}")