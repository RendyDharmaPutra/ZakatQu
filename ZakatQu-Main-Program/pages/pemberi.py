from utils.terminal import clear_screen
from utils.db import read_pemberi
from utils.db import Tambah_data_Pemberi
from utils.db import Edit_data_Pemberi
from utils.db import Hapus_data_Pemberi
from components.table import read_table


def pemberi():
    print("Halaman Pemberi")

    read_table("Data Pemberi", read_pemberi())
        
    print("Tambah[1], Edit[2], Hapus[3]")
    pilihan=input("Masukkan fitur yang dipilih : ")
    match pilihan:
        case '1':
            Tambah_data_Pemberi()
        case '2':
            Edit_data_Pemberi()
        case '3':
            Hapus_data_Pemberi()
        case _:
            print("Input tidak valid")