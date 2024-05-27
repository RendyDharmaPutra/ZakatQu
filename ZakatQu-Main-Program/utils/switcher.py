from typing import List

from pages import login, distribusi, amil, pembayaran, pemberi, penerima



def main_menu(var: str, akun: List[str] | str):
    
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
            if akun != "Takmir" :
                distribusi.distribusi(akun)
                return
            
            print("\nAnda tidak dapat mengakses fitur ini !")
            
            input("Enter untuk kembali ke Halaman utama")
        case '4':
            if akun != "Takmir" :
                pemberi.pemberi()
                return
            
            print("\nAnda tidak dapat mengakses fitur ini !")
            
            input("Enter untuk kembali ke Halaman utama")
        case '5':
            if akun != "Takmir" :
                penerima.penerima()
                return
            
            print("\nAnda tidak dapat mengakses fitur ini !")
            
            input("Enter untuk kembali ke Halaman utama")
        case '6':
            while(True) :
                confirm: str = input("Yakin untuk keluar? (y/n) ")

                if confirm != 'y' and confirm != 'n' :
                    continue
                
                return confirm

        case _:
            print("Input tidak valid!")