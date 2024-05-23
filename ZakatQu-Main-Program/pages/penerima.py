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
            Edit_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 3:
            Hapus_data_Penerima()
            input("Tekan Enter untuk kembali ke menu")
        case 4:
            print("Kembali ke menu sebelumnya ?  ")
            input()

"""Koneksi ke Penerima Zakat"""    
    
def Lihat_data_Penerima():
    cur.execute("Select * From penerima_zakat;")
    data=cur.fetchall()
    for i in data:
        print(i)

def Tambah_data_Penerima(tabel_data, kolom_data) :


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


        data_baru.append(input("Masukkan nama penerima zakat : "))
        data_baru.append(input("Masukkan NIK penerima zakat : "))
        data_baru.append(input("Masukkan alamat penerima zakat : "))
        data_baru.append(input("Masukkan RT/RW penerima zakat : "))
        data_baru.append(input("Masukkan nomor telepon penerima zakat : "))

        QueryInput(data_baru, tabel_data, kolom_data)

        message = "Berhasil menambah Amil"

def Edit_data_Penerima():
    Lihat_data_Penerima()
    id_penerima=(input("Masukkan id penerima yang ingin di edit : "))
    select_query=f"SELECT * FROM  penerima_zakat WHERE id_penerima_zakat ={id_penerima}"
    cur.execute(select_query,(id_penerima,))
    data2=cur.fetchone()

    if data2:
        print('Data saat ini:')
        print(f'id penerima zakat saat ini : {data2[0]}')
        print(f'nama kepala keluarga saat ini: {data2[1]}')
        print(f'no KK penerima zakat saat ini: {data2[2]}')
        print(f'alamat penerima zakat saat ini: {data2[3]}')
        print(f'RT/RW penerima zakat saat ini: {data2[4]}')
        print(f'nomor telepon penerima zakat saat ini: {data2[5]}')

    nama_penerima = input(f"Masukkan nama penerima yang baru : ") or data2[1]
    no_kk = input(f"Masukkan no KK yang baru : ") or data2[2]
    alamat= input(f"Masukkan alamat yang baru : ") or data2[3]
    RtRW = input(f"Masukkan RT/RW yang baru : ") or data2[4]
    telepon = input(f"Masukkan nomor telepon yang baru : ") or data2[5]

    queryUpdate=f'UPDATE penerima_zakat SET nama_kepala_keluarga = %s,no_kk= %s,alamat =%s,"RT/RW"=%s,nomor_telepon=%s WHERE id_penerima_zakat = %s'
    cur.execute(queryUpdate,(nama_penerima,no_kk,alamat,RtRW,telepon,id_penerima))
    print("Data berhasil diperbarui")

def Hapus_data_Penerima():
    Lihat_data_Penerima()
    idPenerima = input('Masukkan id penerima yang ingin dihapus: ')
    query_delete = f"DELETE FROM penerima_zakat WHERE id_penerima_zakat = {idPenerima}"
    cur.execute(query_delete)
    conn.commit()