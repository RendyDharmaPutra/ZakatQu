from utils.db import conn, cur, read_distribusi_with_join
from components.table import read_table
from utils.terminal import clear_screen


def distribusi():
    tabel_data = "distribusi_zakat"
    kolom_data = 'jumlah_paket_zakat, id_amil_zakat, id_bentuk_zakat, id_status_distribusi, id_penerima_zakat'

    message: str = ''

    while True :
        clear_screen()

        print("Halaman Distribusi\n")

        if len(message) > 0 :
            print(f"{message}\n")

        read_table("Data Distribusi", read_distribusi_with_join())

        print("\nTambah(1), Ubah(2), Hapus(3), Keluar(0)")
        fitur = input("Masukkan fitur yang dipilih : ")


        match fitur :
            case '1' :
                tambah_amil(tabel_data, kolom_data)

            case '2' :
                ubah_amil(tabel_data, kolom_data)

            case '3' :
                hapus_amil()
                
            case '0' :
                confirm: str = input("Masukkan 0 untuk keluar ke Halaman Utama : ")

                if confirm == '0' :
                    break

                elif len(confirm) > 0 and confirm != '0' :
                    message = "Input tidak valid"

                    continue

            case _ :
                message = "Input tidak valid"

                continue
        
        message = '' 