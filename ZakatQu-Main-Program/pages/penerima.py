from utils.db import Tambah_data_Penerima
from utils.db import Lihat_data_Penerima
from utils.db import Edit_data_Penerima
from utils.db import Hapus_data_Penerima



def penerima():
    print("Halaman Penerima")
    print('''1. Tambah Penerima \n2. Lihat Penerima \n3. Edit Penerima \n4. Hapus Penerima''')
    Entry = int(input("Masukkan pilihan : "))
    match Entry:
        case 1:
            Tambah_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 2:
            Lihat_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 3:
            Edit_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 4:
            Hapus_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case _:
            print("Input tidak valid")