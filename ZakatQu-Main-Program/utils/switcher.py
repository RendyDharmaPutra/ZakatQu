from typing import List

from pages import login, distribusi, amil, pembayaran, pemberi, penerima



def main_menu(var: str, akun: List[str] | str):
    # switcher = {
    #     '1': login.login(),
    #     '2': amil.amil(),
    #     '3': pembayaran.pembayaran(),
    #     '4': distribusi.distribusi(),
    #     '5': pemberi.pemberi(),
    #     '6': penerima.penerima(),
    # }

    # Placeholder
    match var:
        case '1':
            if akun == "Takmir" :
                amil.amil(akun)
                return ''
                
                # input()
            print("\nAnda tidak memiliki izin!")
            
            input("Enter untuk kembali ke Halaman utama")
        case '2':
            if akun != "Takmir" :
                pembayaran.pembayaran(akun)
                return
            
            print("\nAnda tidak dapat mengakses fitur ini !")
            
            input("Enter untuk kembali ke Halaman utama")
        case '3':
            distribusi.distribusi(akun)
        case '4':
            pemberi.pemberi()
        case '5':
            penerima.penerima()
        case _:
            print("Input tidak valid!")

    # return switcher.get(var, 'Input tidak valid')