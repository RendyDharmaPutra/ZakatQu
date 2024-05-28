from typing import List

from utils import switcher, terminal
from utils.db import conn, cur
from components import list
from pages.login import login
from pages.pemberi import pemberi


if __name__ == '__main__':
    iterate: int = 1



    while(iterate <= 3) :
        terminal.clear_screen()

        akun: List[str] | str = login()

        if(len(akun) > 0) :
            break

        iterate += 1



    if len(akun) < 1 :
        terminal.clear_screen()

        print("Silahkan buka aplikasi kembali")

        
    confirm: str = ''

    while(len(akun) > 0 and confirm != 'y') :
        terminal.clear_screen()

        print(akun)

        list_menu: List[str] = ["Amil zakat", "Pembayaran Zakat", "Distribusi", "Pemberi Zakat", "Penerima Zakat", "Keluar dari aplikasi"]
        list.print_list(list_menu)

        result: str = input("Pilih menu yang dituju : ")
        confirm = switcher.main_menu(result, akun)



    cur.close()
    conn.close()