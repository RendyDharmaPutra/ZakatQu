from utils.terminal import clear_screen
from components.table import read_table
from utils.db import conn, cur, read_penerima, QueryInput,Update_data, Delete_data

def penerima():
    
    nama_tabel = 'penerima_zakat'
    kolom_tabel = 'nama_kepala_keluarga,no_kk,alamat,"RT/RW",nomor_telepon'
    print("Halaman Penerima")
    read_table("Data Penerima", read_penerima())
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

"""Koneksi ke Penerima Zakat"""    
    
# def Lihat_data_Penerima():
#     cur.execute("Select * From penerima_zakat;")
#     data=cur.fetchall()
#     for i in data:
#         print(i)
def Lihat_data_Penerima(no_kk: str = ''):

    search : str = ''

    if len(no_kk) > 0 :
        search = f"WHERE id_penerima_zakat = {no_kk}"

    cur.execute(f"SELECT * FROM penerima_zakat {search}")
    data = cur.fetchall() 

    if data :
        return data



def Tambah_data_Penerima(tabel_data, kolom_data) :


    message: str = ''

    while True :
        data_baru: list[str] = []
        
        
        clear_screen()

        print("Tambah Penerima\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0' :
            return -1
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue


        data_baru.append(input("Masukkan nama penerima zakat : "))
        data_baru.append(input("Masukkan NIK penerima zakat : "))
        data_baru.append(input("Masukkan alamat penerima zakat : "))
        data_baru.append(input("Masukkan RT/RW penerima zakat : "))
        data_baru.append(input("Masukkan nomor telepon penerima zakat : "))

        QueryInput(data_baru, tabel_data, kolom_data)

        message = "Berhasil menambah Penerima"

def Edit_data_Penerima(tabel_data, kolom_data):
    message: str = ''

    while True:
        data_baru: list[str] = []

        clear_screen()

        print("Ubah Penerima\n")

        if len(message) > 0:
            print(f"{message}\n")

        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0':
            return -1

        elif len(confirm) > 0 and confirm != '0':
            message = "Input tidak valid"
            continue

        read_table("Data Penerima", Lihat_data_Penerima())

        IdDipilih = input("Masukkan id penerima yang ingin diubah : ")
        data_baru = Lihat_data_Penerima(IdDipilih)[0]
        print(data_baru)
        input()

        input()

        if data_baru == 0:
            message = "id penerima yang dimasukkan tidak terdaftar!"
            continue

        NamaPenerima = input("Masukkan nama penerima yang baru : ") or data_baru[1]
        NoKK = input("Masukkan no KK yang baru : ") or data_baru[2]
        Alamat = input("Masukkan alamat yang baru : ") or data_baru[3]
        RtRw = input("Masukkan RT/RW yang baru : ") or data_baru[4]
        Telepon = input("Masukkan nomor telepon yang baru : ") or data_baru[5]

        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            pemberi()
        
        else:
            Update_data('penerima_zakat',f"nama_kepala_keluarga='{NamaPenerima}',no_kk='{NoKK}',alamat='{Alamat}',\"RT/RW\"='{RtRw}',nomor_telepon='{Telepon}' WHERE id_penerima_zakat={IdDipilih}")
                    
        message = "Berhasil mengubah data penerima"

# def Hapus_data_Penerima():
#     Lihat_data_Penerima()
#     idPenerima = input('Masukkan id penerima yang ingin dihapus: ')
#     query_delete = f"DELETE FROM penerima_zakat WHERE id_penerima_zakat = {idPenerima}"
#     cur.execute(query_delete)
#     conn.commit()
def Hapus_data_Penerima(tabel_data, kolom_data):
    message: str = ''

    while True:
        clear_screen()

        print("Hapus Penerima\n")

        if len(message) > 0:
            print(f"{message}\n")

        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0':
            return -1

        elif len(confirm) > 0 and confirm != '0':
            message = "Input tidak valid"
            continue

        read_table("Data Penerima", Lihat_data_Penerima())

        idPenerima = input("Masukkan id penerima yang ingin dihapus : ")

        if idPenerima == -1:
            message = "id penerima yang dimasukkan tidak terdaftar!"
            continue
        
        Delete_data(tabel_data,"id_penerima_zakat",idPenerima)

        message = "Berhasil menghapus data penerima"