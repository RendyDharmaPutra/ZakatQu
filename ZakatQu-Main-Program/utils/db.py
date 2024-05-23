import psycopg2


conn = psycopg2.connect(database='ZakatQu', user='postgres', password='rendydp424', host='localhost', port=5432)
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
    
def Update_data(NamaTabel, Query):
    
    cur.execute(f"UPDATE {NamaTabel} SET {Query}")
    conn.commit()
    
def Delete_data(nama_tabel, nama_kolom, idData):
    
    cur.execute(f"DELETE FROM {nama_tabel} WHERE {nama_kolom} = {idData}")
    conn.commit()

def searchPemberi(Input):
    cur.execute(f"SELECT * FROM pemberi_zakat where id_pemberi_zakat = {Input}")
    data = cur.fetchall()
    if data:
        return data
    else:
        return "Data Tidak Ada"

def read_pemberi(id: str = '', nik: str = ''):

    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_pemberi_zakat = {id}"
    elif len(nik) > 0 :
        search = f"WHERE nik = '{nik}'"

    cur.execute(f"""
    select p.id_pemberi_zakat, p.nama_pemberi_zakat, p.nik, p.alamat, p."RT/RW", p.nomor_telepon, pz.nama_pembayaran_zakat
    from pemberi_zakat p join status_pembayaran_zakat pz on (p.id_status_pembayaran_zakat = pz.id_status_pembayaran_zakat)
    {search} ORDER BY id_pemberi_zakat
    """)
    data=cur.fetchall()
    
    if data :
        return data
    
def read_pembayaran(id: str = ''):

    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_pembayaran = {id}"

    cur.execute(f"SELECT * FROM pembayaran_zakat {search} ORDER BY id_pembayaran")
    data=cur.fetchall()
    
    if data :
        return data
    
def read_pembayaran_with_join(idpembayaran: str = '', idpemberi: str = ''):

    search: str = ''

    if len(idpembayaran) > 0 :
        search = f"where pz.id_pembayaran = {idpembayaran}"
    elif len(idpemberi) > 0 :
        search = f"where pz.id_pemberi_zakat = {idpemberi}"

    cur.execute(f"""
    select pz.id_pembayaran, pza.nama_pemberi_zakat, pz.besar_pemberian, to_char(pz.tanggal_pemberian, 'DD/MM/YY'), j.nama_jenis_zakat, b.nama_bentuk_zakat, a.nama_amil_zakat, pz.id_pemberi_zakat
    from pembayaran_zakat pz join pemberi_zakat pza on (pz.id_pemberi_zakat = pza.id_pemberi_zakat)
    join jenis_zakat j on (pz.id_jenis_zakat = j.id_jenis_zakat)
    join bentuk_zakat b on (pz.id_bentuk_zakat = b.id_bentuk_zakat)
    join amil_zakat a on (pz.id_amil_zakat = a.id_amil_zakat)
    {search}
    Order by pz.id_pembayaran
                """)
    data=cur.fetchall()
    
    if data :
        return data

    
def read_amil(nik: str = '') -> list[tuple] :

    search: str = ''

    if len(nik) > 0 :
        search = f"WHERE nik = '{nik}'"
        

    cur.execute(f"SELECT * FROM amil_zakat {search}")
    data = cur.fetchall()

    if data :
        return data
    
    return -1

def del_amil(nik: str) :
    
    cur.execute(f"DELETE FROM amil_zakat WHERE nik = '{nik}'")
    conn.commit()

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
