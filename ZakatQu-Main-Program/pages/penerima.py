from utils.terminal import clear_screen
from components.table import read_table
from utils.db import conn, cur

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

"""Koneksi ke Penerima Zakat"""

def read_penerima_join(no_kk : str = '', id : str = ''):
    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_penerima_zakat = {id}"
    elif len(no_kk) > 0 :
        search = f"WHERE nik = '{no_kk}'"

    cur.execute(f"""
    select pz.id_penerima_zakat, pz.nama_kepala_keluarga, pz.no_kk, pz.alamat, pz."RT/RW", pz.nomor_telepon, sd.nama_status_distribusi
    from penerima_zakat pz
    join distribusi_zakat dz on pz.id_penerima_zakat = dz.id_penerima_zakat
    join status_distribusi sd on dz.id_status_distribusi = sd.id_status_distribusi
   {search} order by id_penerima_zakat
    """)
    data=cur.fetchall()
    
    if data :
        return data
    
    
def Lihat_data_Penerima():
    cur.execute("Select * From penerima_zakat;")
    data=cur.fetchall()
    for i in data:
        print(i)


def Tambah_data_Penerima():
    nama_kepala_penerima = input("Masukkan nama penerima zakat : ")
    noKK_penerima=input("Masukkan NIK penerima zakat : ")
    alamat_penerima=input("Masukkan alamat penerima zakat : ")
    RtRw_penerima=input("Masukkan RT/RW penerima zakat : ")
    telepon_penerima= input("Masukkan nomor telepon penerima zakat : ")

    query=f'INSERT INTO penerima_zakat(nama_kepala_keluarga,no_kk,alamat,"RT/RW",nomor_telepon) VALUES(%s,%s,%s,%s,%s)'
    cur.execute(query,(nama_kepala_penerima,noKK_penerima,alamat_penerima,RtRw_penerima,telepon_penerima))
    print("Data berhasil ditambahkan")
    conn.commit()

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