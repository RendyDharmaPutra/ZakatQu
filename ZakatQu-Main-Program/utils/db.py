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

def Update_data(NamaTabel, Query):
    
    cur.execute(f"UPDATE {NamaTabel} SET {Query}")
    conn.commit()
    
def Delete_data(nama_tabel, nama_kolom, idData):
    
    cur.execute(f"DELETE FROM {nama_tabel} WHERE {nama_kolom} = {idData}")
    conn.commit()

def Delete_data_varchar(nama_tabel, nama_kolom, idData):
    
    cur.execute(f"DELETE FROM {nama_tabel} WHERE {nama_kolom} = '{idData}'")
    conn.commit()

# =========================== #\
    
def read_amil(nik: str = '') -> list[tuple] :

    search: str = ''

    if len(nik) > 0 :
        search = f"WHERE nik = '{nik}'"
        

    cur.execute(f"SELECT * FROM amil_zakat {search}")
    data = cur.fetchall()

    if data :
        return data
    
    return -1
    
def read_penerima(no_kk : str = '', id : str = ''):
    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_penerima_zakat = {id}"
    elif len(no_kk) > 0 :
        search = f"WHERE nik = '{no_kk}'"

    cur.execute(f"""select* from penerima_zakat {search} order by id_penerima_zakat""")
    data=cur.fetchall()
    
    if data :
        return data

def read_Daftar_Pemberi():
    cur.execute("Select * From pemberi_zakat;")
    data=cur.fetchall()

    for i in data:
        print(i)

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
    select pz.id_pembayaran, pza.nama_pemberi_zakat, pz.besar_pemberian, to_char(pz.tanggal_pemberian, 'DD/MM/YY'), b.nama_bentuk_zakat, j.nama_jenis_zakat, a.nama_amil_zakat, pz.id_pemberi_zakat
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
    
def read_distribusi_with_join(iddistribusi: str = ''):

    search: str = ''

    if len(iddistribusi) > 0 :
        search = f"where pz.id_pembayaran = {iddistribusi}"

    cur.execute(f"""
    select dz.id_distribusi_zakat, pz.nama_kepala_keluarga, bz.nama_bentuk_zakat, ddz.jumlah_zakat, sd.nama_status_distribusi 
    from distribusi_zakat dz join detail_distribusi_zakat ddz on (dz.id_distribusi_zakat = ddz.id_distribusi_zakat)
    join penerima_zakat pz on (pz.id_penerima_zakat = dz.id_penerima_zakat)
    join bentuk_zakat bz on (bz.id_bentuk_zakat = ddz.id_bentuk_zakat)
    join status_distribusi sd on (sd.id_status_distribusi = dz.id_status_distribusi) 
    {search}
    Order by dz.id_distribusi_zakat
                """)
    data=cur.fetchall()
    
    if data :
        return data

def read_penerima_in_distribusi(id : str = ''):
    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_penerima_zakat = {id}"

    cur.execute(f"""select* from distribusi_zakat {search} order by id_penerima_zakat""")
    data=cur.fetchall()
    
    if data :
        return data
    
def read_distribusi(id : str = ''):
    search: str = ''

    if len(id) > 0 :
        search = f"WHERE id_distribusi_zakat = {id}"

    cur.execute(f"""select* from distribusi_zakat {search} order by id_distribusi_zakat""")
    data=cur.fetchall()
    
    if data :
        return data
    
def read_detail_distribusi(id : str = '', bentuk_zakat : int = 0):
    search: str = ''

    if len(id) > 0 and bentuk_zakat > 0 :
        search = f"WHERE id_distribusi_zakat = {id} and id_bentuk_zakat = {bentuk_zakat}"

    cur.execute(f"""select* from detail_distribusi_zakat {search} order by id_distribusi_zakat""")
    data=cur.fetchall()
    
    if data :
        return data
    
def Read_Banyak_Zakat():
    cur.execute("""
    select bz.nama_bentuk_zakat, sum(pz.besar_pemberian)
    from pembayaran_zakat pz full join bentuk_zakat bz on (pz.id_bentuk_zakat = bz.id_bentuk_zakat)
    group by bz.nama_bentuk_zakat 
                """)
    
    data = cur.fetchall()
    return data

def Read_Banyak_Zakat_From_Distribusi():
    cur.execute("""
    select bz.nama_bentuk_zakat, sum(ddz.jumlah_zakat)
    from detail_distribusi_zakat ddz full join bentuk_zakat bz on (ddz.id_bentuk_zakat = bz.id_bentuk_zakat)
    group by bz.nama_bentuk_zakat 
                """)
    
    data = cur.fetchall()
    return data


def read_pemberi(nik: str = '') -> list[tuple] :

    search: str = ''

    if len(nik) > 0 :
        search = f"WHERE nik = '{nik}'"
        

    cur.execute(f"SELECT * FROM pemberi_zakat {search}")
    data = cur.fetchall()

    if data :
        return data
    
    return -1
    # select pz.id_penerima_zakat, pz.nama_kepala_keluarga, pz.no_kk, pz.alamat, pz."RT/RW", pz.nomor_telepon, sd.nama_status_distribusi
    # from penerima_zakat pz
    # join distribusi_zakat dz on pz.id_penerima_zakat = dz.id_penerima_zakat
    # join status_distribusi sd on dz.id_status_distribusi = sd.id_status_distribusi
