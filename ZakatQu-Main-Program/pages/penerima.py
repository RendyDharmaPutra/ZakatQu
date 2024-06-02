from utils.db import conn, cur, read_penerima, QueryInput,Update_data, Delete_data
from utils.terminal import clear_screen
from components.table import read_table

def penerima(akun):
    
    nama_tabel = 'penerima_zakat'
    kolom_tabel = 'nama_kepala_keluarga,no_kk,alamat,"RT/RW",nomor_telepon'
    print("Halaman Penerima")
    read_table("Data Penerima", read_penerima())
    
    if akun == "Takmir":
        input()
        return
    
    print('''1. Tambah Penerima \n2. Edit Penerima \n3. Hapus Penerima \n4. Kembali ke menu sebelumnya''')
    
    Entry = int(input("Masukkan pilihan : "))
    match Entry:
        case 1:
            Tambah_data_Penerima(nama_tabel, kolom_tabel)
            input("Tekan Enter untuk kembali ke menu")
        case 2:
            Edit_data_Penerima(nama_tabel,kolom_tabel)
            input("Tekan Enter untuk kembali ke menu")
        case 3:
            Hapus_data_Penerima(nama_tabel,kolom_tabel)
            input("Tekan Enter untuk kembali ke menu")
        case 4:
            print("Kembali ke menu sebelumnya ?  ")
            input()

        print("Halaman Penerima\n")

        if len(msg) > 0:
            print(msg)

        read_table("Data Penerima", read_penerima())
            
        print('''1. Tambah Penerima \n2. Edit Penerima \n3. Hapus Penerima \n4. Kembali ke menu sebelumnya''')
        
        Entry = input("Masukkan pilihan : ")

        match Entry :
            case '1':
                Tambah_data_Penerima(nama_tabel, kolom_tabel)
            case '2':
                Edit_data_Penerima(nama_tabel,kolom_tabel)
            case '3':
                Hapus_data_Penerima(nama_tabel,kolom_tabel)
            case '4':
                confirm: str = input("Masukkan 0 untuk keluar ke Halaman Utama : ")

                if confirm == '0' :
                    return -1

                elif len(confirm) > 0 and confirm != '0' :
                    msg = "Input tidak valid"

                    continue

            case _ :
                msg = "Input tidak valid"
                continue

def Lihat_data_Penerima(no_kk: str = ''):
    search : str = ''

    if len(no_kk) > 0 :
        search = f"WHERE id_penerima_zakat = {no_kk}"
    cur.execute(f"SELECT * FROM penerima_zakat {search}")
    data = cur.fetchall() 

    if data :
        return data
    else :
        return 0

def Tambah_data_Penerima(tabel_data, kolom_data) :
    message: str = ''

    while True :
        data_baru: list[str] = []
        clear_screen()

        read_table("Data Penerima", read_penerima())
        print("Tambah Penerima\n")
        
        if len(message) > 0 :
            print(f"{message}\n")

        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")
        if confirm == '0' :
            return
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            continue

        data_baru.append(input("Masukkan nama penerima zakat : "))
        data_baru.append(input("Masukkan NIK penerima zakat : "))
        data_baru.append(input("Masukkan alamat penerima zakat : "))
        data_baru.append(input("Masukkan RT/RW penerima zakat : "))
        data_baru.append(input("Masukkan nomor telepon penerima zakat : "))
        
        if len(data_baru) < 5:
            message = "Input tidak valid"

        if (len(data_baru[0]) == 0 or len(data_baru[1]) == 0 or 
            len(data_baru[2]) == 0 or len(data_baru[3]) == 0 or len(data_baru[4]) == 0):
            message = "Data tidak boleh ada kosong"
            continue

        QueryInput(data_baru, tabel_data, kolom_data)
        message = "Berhasil menambah Penerima"
        # if QueryInput(data_baru, tabel_data, kolom_data) : 
        #     message = "Berhasil menambah Penerima"
        #     break
        # else :
        #     message = "Gagal menambah Penerima"
        #     continue

def Edit_data_Penerima(tabel_data, kolom_data):
    message: str = ''
    while True:
        data_baru: list[str] = []
        clear_screen()

        read_table("Data Penerima", Lihat_data_Penerima())
        print("Ubah Penerima\n")
        if len(message) > 0:
            print(f"{message}\n")

        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")
        if confirm == '0':
            return
        elif len(confirm) > 0 and confirm != '0':
            message = "Input tidak valid"
            continue

        IdDipilih = input("Masukkan id penerima yang ingin diubah : ")

        if len(IdDipilih) == 0:
            message = "id penerima yang dimasukkan tidak boleh kosong!"
            continue

        data_baru = Lihat_data_Penerima(IdDipilih)[0]

        print(data_baru)
        if len(data_baru) == 0:
            message = "id penerima yang dimasukkan tidak terdaftar!"
            continue

        NamaPenerima = input("Masukkan nama penerima yang baru : ") or data_baru[1]
        #Tabel Nomor KK
        NoKK = input("Masukkan no KK yang baru : ") or data_baru[2]
        #Tabel Alamat Penerima
        Alamat = input("Masukkan alamat yang baru : ") or data_baru[3]
        #Tabel RT/RW
        RtRw = input("Masukkan RT/RW yang baru : ") or data_baru[4]
        #Tabel Nomor Telepon
        Telepon = input("Masukkan nomor telepon yang baru : ") or data_baru[5]

        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        if Konfirmasi.lower() == "0":
            break

        Update_data(tabel_data, f"id_penerima_zakat = {IdDipilih}, nama_kepala_keluarga = '{NamaPenerima}', no_kk = '{NoKK}', alamat = '{Alamat}', \"RT/RW\" = '{RtRw}', nomor_telepon = '{Telepon}' WHERE id_penerima_zakat = {IdDipilih}")

        message = "Berhasil mengubah data penerima"


def Hapus_data_Penerima(tabel_data, kolom_data):
    message: str = ''

    while True:
        clear_screen()
        print("Hapus Penerima\n")

        if len(message) > 0:
            print(f"{message}\n")

        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")
        if confirm == '0':
            return
        elif len(confirm) > 0 and confirm != '0':
            message = "Input tidak valid"
            continue

        read_table("Data Penerima", Lihat_data_Penerima())

        idPenerima = input("Masukkan id penerima yang ingin dihapus : ")
        if len (idPenerima) == 0:
            message = "id penerima yang dimasukkan tidak boleh kosong!"
            continue

        data_penerima = Lihat_data_Penerima(idPenerima)
        if data_penerima == 0:
            message = "id penerima yang dimasukkan tidak terdaftar!"
            continue

        # if idPenerima == -1:
        #     message = "id penerima yang dimasukkan tidak terdaftar!"
        #     continue
        
        Konfirmasi = input("Tekan Enter Untuk Hapus Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            break

        Delete_data(tabel_data,"id_penerima_zakat",idPenerima)

        message = "Berhasil menghapus data penerima"