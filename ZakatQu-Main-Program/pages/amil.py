from utils.db import read_amil, QueryInput
from utils.terminal import clear_screen

def amil(akun: str):
    tabel_data = "amil_zakat"
    kolom_data = 'nama_amil_zakat, nik, alamat, "RT/RW", nomor_telepon'

    message: str = ''

    while akun == "Takmir" :
        clear_screen()

        print("Halaman Amil\n")

        if len(message) > 0 :
            print(f"{message}\n")

        print(read_amil())

        print("\nTambah(1), Ubah(2), Hapus(3), Keluar(0)")
        fitur = input("Masukkan fitur yang dipilih : ")


        match fitur :
            case '1' :
                tambah_amil(tabel_data, kolom_data)

            case '2' :
                ubah_amil(tabel_data, kolom_data)

            case '3' :
                hapus_amil(tabel_data, kolom_data)
                
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

        data_search = read_amil(data_baru[1])

        if data_search != -1 :
            message = "NIK yang dimasukkan sudah terdaftar!"

            # Metode message 1
            # print("NIK yang dimasukkan sudah terdaftar!")
            # input("Tekan Enter untuk kembali")

            continue


        # Insert Into Database
        QueryInput(data_baru, tabel_data, kolom_data)

        message = "Berhasil menambah Amil"






def ubah_amil() :
    print("Ubah")
    
def hapus_amil() :
    print("Hapus")