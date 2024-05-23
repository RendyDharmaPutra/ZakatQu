from utils.terminal import clear_screen
from components.table import read_table
from utils.db import conn, cur, read_penerima_join, QueryInput

def penerima():
    
    nama_tabel = 'penerima_zakat'
    kolom_tabel = 'nama_kepala_keluarga,no_kk,alamat,"RT/RW",nomor_telepon'
    print("Halaman Penerima")
    read_table("Data Penerima", read_penerima_join())
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
        search = f"WHERE no_kk = '{search}'"

    cur.execute(f"SELECT * FROM penerima_zakat {search}")
    data = cur.fetchall() 

    if data :
        return data
    
    return -1



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

        data_baru = Lihat_data_Penerima(input("Masukkan id penerima yang ingin diubah : "))

        input()

        if data_baru == 0:
            message = "id penerima yang dimasukkan tidak terdaftar!"
            continue

        data_baru[1] = input("Masukkan nama penerima yang baru : ") or data_baru[1]
        data_baru[2] = input("Masukkan no KK yang baru : ") or data_baru[2]
        data_baru[3] = input("Masukkan alamat yang baru : ") or data_baru[3]
        data_baru[4] = input("Masukkan RT/RW yang baru : ") or data_baru[4]
        data_baru[5] = input("Masukkan nomor telepon yang baru : ") or data_baru[5]

        # Insert Into Database
        QueryInput(data_baru, tabel_data, kolom_data)
        
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

        query_delete = f"DELETE FROM penerima_zakat WHERE id_penerima_zakat = {idPenerima}"
        cur.execute(query_delete)
        conn.commit()

        message = "Berhasil menghapus data penerima"