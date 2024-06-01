from utils.db import Update_data, read_amil, QueryInput, Delete_data, Delete_data_varchar
from utils.terminal import clear_screen
from components.table import read_table
from utils.validate import validate_empty


def amil(akun: str):
    tabel_data = "amil_zakat"
    kolom_data = 'nama_amil_zakat, nik, alamat, "RT/RW", nomor_telepon'

    message: str = ''

    while akun == "Takmir" :
        clear_screen()

        print("Halaman Amil\n")

        if len(message) > 0 :
            print(f"{message}\n")

        read_table("Data Amil", read_amil())

        print("\nTambah(1), Ubah(2), Hapus(3), Keluar(0)")
        fitur = input("Masukkan fitur yang dipilih : ")


        match fitur :
            case '1' :
                tambah_amil(tabel_data, kolom_data)

            case '2' :
                ubah_amil(tabel_data, kolom_data)

            case '3' :
                hapus_amil(tabel_data)
                
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



def tambah_amil(tabel_data, kolom_data) :


    message: str = ''

    while True :
        data_baru: list[str] = []
        
        
        clear_screen()

        print("Tambah Amil\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0' :
            return -1
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue


        data_baru.append(input("\nMasukkan nama Amil : "))
        data_baru.append(input("Masukkan NIK amil : "))
        data_baru.append(input("Masukkan Alamat Rumah Amil : "))
        data_baru.append(input("Masukkan RT/RW amil : "))
        data_baru.append(input("Masukkan Nomor Telepon Amil : "))

        # Validasi
        message = validate_empty(data_baru)

        if len(message) > 0 :
            continue



        data_search = read_amil(data_baru[1])

        if data_search != -1 :
            message = "NIK yang dimasukkan sudah terdaftar!"

            continue


        # Insert Into Database
        # for i in track(range(100), description="Menambah Data...") :
        QueryInput(data_baru, tabel_data, kolom_data)

        message = "Berhasil menambah Amil"



def ubah_amil(tabel_data, kolom_data) :
    message: str = ''

    while True :
        data_baru: list[str] = []
        
        
        clear_screen()

        print("Ubah Amil\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0' :
            return -1
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue


        read_table("Data Amil", read_amil())

        data_baru = input("Masukkan NIK data amil yang ingin diubah : ")
        
        if len(data_baru) == 0 :
            message = "NIK yang dimasukkan tidak boleh kosong!"
            
            continue

        data_baru = read_amil(data_baru)
        
        if data_baru == -1 :
            message = "NIK yang dimasukkan tidak terdaftar!"

            continue

        
        clear_screen()

        read_table("Data Amil", data_baru)

        data_baru = list(data_baru[0])
        
        data_baru[1] = input("Masukkan Nama Amil : ") or data_baru[1]
        data_baru[2] = input("Masukkan NIK amil : ") or data_baru[2]
        data_baru[3] = input("Masukkan Alamat Rumah Amil : ") or data_baru[3]
        data_baru[4] = input("Masukkan RT/RW amil : ") or data_baru[4]
        data_baru[5] = input("Masukkan Nomor Telepon Amil : ") or data_baru[5]

        # Validasi
        message = validate_amil(data_baru[1:-1])

        if len(message) > 0 :
            continue

        print(data_baru)


        # Insert Into Database
        Update_data(tabel_data, f"id_amil_zakat = {data_baru[0]}, nama_amil_zakat = '{data_baru[1]}', nik = '{data_baru[2]}', alamat = '{data_baru[3]}', \"RT/RW\" = '{data_baru[4]}', nomor_telepon =  {data_baru[5]} WHERE id_amil_zakat = {data_baru[0]}")
        
        message = "Berhasil mengubah Amil"
    


def hapus_amil(tabel_data) :
    message: str = ''

    while True :
        data: str = ''
        
        
        clear_screen()

        print("Hapus Amil\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm: str = input("Masukkan 0 untuk keluar dari fitur : \n")

        if confirm == '0' :
            return -1
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue


        read_table("Hapus Amil", read_amil())

        data_baru = input("\nMasukkan NIK Amil : ")
        
        if len(data_baru) == 0 :
            message = "NIK yang dimasukan tidak boleh kosong!"

            continue

        data_baru = read_amil(data_baru)

        if data_baru == -1 :
            message = "NIK yang dimasukkan tidak terdaftar!"

            continue

        Konfirmasi = input("Tekan Enter Untuk Hapus Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            continue
        

        Delete_data_varchar(tabel_data, 'nik', f'{data_baru}')

        message = "Berhasil menghapus Amil"