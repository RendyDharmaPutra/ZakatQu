from utils.db import read_amil
from utils.terminal import clear_screen

def amil(akun: str):

    while akun == "Takmir" :
        clear_screen()

        print("Halaman Amil\n")

        data = read_amil()
        print(data)

        print("\nTambah(1), Ubah(2), Hapus(3), Keluar(0)")
        fitur = input("Masukkan fitur yang dipilih : ")

        match fitur :
            case '1' :
                # clear_screen()
                tambah_amil()

            case '2' :
                # clear_screen()
                ubah_amil()

            case '3' :
                # clear_screen()
                hapus_amil()

        input()



def tambah_amil() :
    print("Tambah")

def ubah_amil() :
    print("Ubah")
    
def hapus_amil() :
    print("Hapus")