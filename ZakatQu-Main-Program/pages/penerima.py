from utils.terminal import clear_screen
from utils.db import read_penerima_join
from components.table import read_table
from utils.db import Tambah_data_Penerima
from utils.db import Lihat_data_Penerima
from utils.db import Edit_data_Penerima
from utils.db import Hapus_data_Penerima



def penerima():
    print("Halaman Penerima")
    read_table("Data Penerima", read_penerima_join())
    print('''1. Tambah Penerima \n2. Edit Penerima \n3. Hapus Penerima \n4. Kembali ke menu sebelumnya''')
    Entry = int(input("Masukkan pilihan : "))
    match Entry:
        case 1:
            Tambah_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 2:
            Edit_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 3:
            Hapus_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 4:
            print("Kembali ke menu sebelumnya ?  ")
            input()