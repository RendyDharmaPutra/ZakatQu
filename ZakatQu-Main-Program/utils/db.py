import psycopg2


conn = psycopg2.connect(database='ZakatQu', user='postgres', password='12345678', host='localhost', port=5432)
cur = conn.cursor()

# UNIVERSAL================== #

def login_query(username: str, password: str) -> list[tuple] :
    cur.execute(f"SELECT * FROM amil_zakat WHERE left(nik, 5)= '{username}' AND right(nik, 5)= '{password}';")
    data = cur.fetchall()
    return data

def QueryInput(InputQuery, NamaTabel, NamaKolom):
    cur.execute("INSERT INTO " + NamaTabel + " " + f'({NamaKolom})' + " VALUES " + f'{InputQuery}'.replace("[", "(").replace("]", ")"))
    conn.commit()

# =========================== #

def read_Daftar_Pemberi():
    cur.execute("Select * From pemberi_zakat;")
    data=cur.fetchall()

    for i in data:
        print(i)

def Tambah_data_Pemberi():
    nama_pemberi = input("Masukkan nama pemberi zakat : ")
    nik_pemberi=input("Masukkan NIK pemberi zakat : ")
    alamat_pemberi=input("Masukkan alamat pemberi zakat : ")
    RtRw_pemberi=input("Masukkan RT/RW pemberi zakat : ")
    telepon_pemberi= input("Masukkan nomor telepon pemberi zakat : ")
    status_bayar=int(input("Masukkan status pembayaran : "))

    query=f'INSERT INTO pemberi_zakat(nama_pemberi_zakat,nik,alamat,"RT/RW",nomor_telepon,id_status_pembayaran_zakat) VALUES(%s,%s,%s,%s,%s,%s)'
    cur.execute(query,(nama_pemberi,nik_pemberi,alamat_pemberi,RtRw_pemberi,telepon_pemberi,status_bayar))
    print("Data berhasil ditambahkan")

def Edit_data_Pemberi():
    read_Daftar_Pemberi()
    id_dipilih=(input("Masukkan id pemberi yang ingin di edit : "))
    select_query=f"SELECT * FROM  pemberi_zakat WHERE id_pemberi_zakat ={id_dipilih}"
    cur.execute(select_query,(id_dipilih))
    data2=cur.fetchone()

    if data2:
        print('Data saat ini:')
        print(f'id pemberi zakat saat ini : {data2[0]}')
        print(f'nama pemberi zakat saat ini: {data2[1]}')
        print(f'nik pemberi zakat saat ini: {data2[2]}')
        print(f'alamat pemberi zakat saat ini: {data2[3]}')
        print(f'RT/RW pemberi zakat saat ini: {data2[4]}')
        print(f'nomor telepon pemberi zakat saat ini: {data2[5]}')
        print(f'status pembayaran saat ini : {data2[6]}')

    nama_pemberi = input(f"Masukkan nama pemberi yang baru : ") or data2[1]
    nik = input(f"Masukkan nik yang baru : ") or data2[2]
    alamat= input(f"Masukkan alamat yang baru : ") or data2[3]
    RtRW = input(f"Masukkan RT/RW yang baru : ") or data2[4]
    telepon = input(f"Masukkan nomor telepon yang baru : ") or data2[5]
    statusBayar= input(f"Masukkan status pembayaran yang baru : ") or data2[6]
    statusBayar=int(statusBayar)

    queryUpdate=f'UPDATE pemberi_zakat SET nama_pemberi_zakat = %s,nik= %s,alamat =%s,"RT/RW"=%s,nomor_telepon=%s,id_status_pembayaran_zakat=%s WHERE id_pemberi_zakat = %s'
    cur.execute(queryUpdate,(nama_pemberi,nik,alamat,RtRW,telepon,statusBayar,id_dipilih))
    print("Data berhasil diperbarui")

def Hapus_data_Pemberi():
    read_Daftar_Pemberi()
    idPemberi = input('Masukkan id mata kuliah yang ingin dihapus: ')
    query_delete = f"DELETE FROM mata_kuliah WHERE id_mata_kuliah = {idPemberi}"
    cur.execute(query_delete)
    print("Data berhasil dihapus")

def UpdatePemberi(InputPemberi):
    cur.execute(f"UPDATE pemberi_zakat SET id_status_pembayaran_zakat = 1 where id_pemberi_zakat = '{InputPemberi}'")
    conn.commit()

def searchPemberi(Input):
    cur.execute(f"SELECT * FROM pemberi_zakat where id_pemberi_zakat = {Input}")
    data = cur.fetchall()
    if data:
        return data
    else:
        return "Data Tidak Ada"

def ReadData():
    Query = "SELECT * FROM pemberi_zakat"
    cur.execute(Query)
    data=cur.fetchall()

    for i in data:
        print(str(i))
    
def read_amil(nik: str = '') -> list[tuple] :

    search: str = ''

    if len(nik) > 0 :
        # cur.execute(f"SELECT * FROM amil_zakat")
        search = f"WHERE nik = '{nik}'"
        

    cur.execute(f"SELECT * FROM amil_zakat {search}")
    data = cur.fetchall()

    return data

"""Koneksi ke Penerima Zakat"""

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
def Lihat_data_Penerima():
    cur.execute("Select * From penerima_zakat;")
    data=cur.fetchall()
    for i in data:
        print(i)

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
