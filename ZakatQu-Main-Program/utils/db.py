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
    
def Update_data(NamaTabel, Query):
    
    cur.execute(f"UPDATE {NamaTabel} SET {Query}")
    conn.commit()
    
def Delete_data(nama_tabel, nama_kolom, idData):
    
    cur.execute(f"DELETE FROM {nama_tabel} WHERE {nama_kolom} = {idData}")
    conn.commit()

# def searchPemberi(Input):
#     cur.execute(f"SELECT * FROM pemberi_zakat where id_pemberi_zakat = {Input}")
#     data = cur.fetchall()
#     if data:
#         return data
#     else:
#         return "Data Tidak Ada"

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

