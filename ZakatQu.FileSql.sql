CREATE TABLE amil_zakat (
    id_amil_zakat   SERIAL NOT NULL,
    nama_amil_zakat VARCHAR(50) NOT NULL,
    nik             VARCHAR(50) NOT NULL,
    alamat          VARCHAR(50) NOT NULL,
    "RT/RW"         VARCHAR(10) NOT NULL,
    nomor_telepon   VARCHAR(15) NOT NULL
);

ALTER TABLE amil_zakat ADD CONSTRAINT amil_zakat_pk PRIMARY KEY ( id_amil_zakat );

CREATE TABLE bentuk_zakat (
    id_bentuk_zakat   INTEGER NOT NULL,
    nama_bentuk_zakat VARCHAR(50) NOT NULL
);

ALTER TABLE bentuk_zakat ADD CONSTRAINT bentuk_zakat_pk PRIMARY KEY ( id_bentuk_zakat );

CREATE TABLE distribusi_zakat (
    id_distribusi_zakat     SERIAL NOT NULL,
    jumlah_paket_zakat      INTEGER NOT NULL,
    id_amil_zakat           INTEGER NOT NULL,
    id_bentuk_zakat         INTEGER NOT NULL, 
    id_status_distribusi    INTEGER NOT NULL,
	id_penerima_zakat		INTEGER NOT NULL
);

ALTER TABLE distribusi_zakat ADD CONSTRAINT distribusi_zakat_pk PRIMARY KEY ( id_distribusi_zakat );

CREATE TABLE jenis_zakat (
    id_jenis_zakat   INTEGER NOT NULL,
    nama_jenis_zakat VARCHAR(50) NOT NULL
);

ALTER TABLE jenis_zakat ADD CONSTRAINT jenis_zakat_pk PRIMARY KEY ( id_jenis_zakat );

CREATE TABLE pembayaran_zakat (
    id_pembayaran           SERIAL NOT NULL,
    besar_pemberian         INTEGER NOT NULL,
    tanggal_pemberian       DATE NOT NULL,
    id_amil_zakat           INTEGER NOT NULL,
    id_pemberi_zakat        INTEGER NOT NULL,
    id_bentuk_zakat         INTEGER NOT NULL,
    id_jenis_zakat          INTEGER NOT NULL
);

ALTER TABLE pembayaran_zakat ADD CONSTRAINT pembayaran_zakat_pk PRIMARY KEY ( id_pembayaran );

CREATE TABLE pemberi_zakat (
    id_pemberi_zakat        SERIAL NOT NULL,
    nama_pemberi_zakat      VARCHAR(50) NOT NULL,
    nik                     VARCHAR(16) NOT NULL,
    alamat                  VARCHAR(50) NOT NULL,
    "RT/RW"                 VARCHAR(10) NOT NULL,
    nomor_telepon           VARCHAR(15) NOT NULL, 
    id_status_pembayaran_zakat INTEGER NOT NULL
);

ALTER TABLE pemberi_zakat ADD CONSTRAINT pemberi_zakat_pk PRIMARY KEY ( id_pemberi_zakat );

CREATE TABLE penerima_zakat (
    id_penerima_zakat       SERIAL NOT NULL,
    nama_kepala_keluarga    VARCHAR(50) NOT NULL,
    No_KK                  	VARCHAR(16) NOT NULL,
    alamat                  VARCHAR(50) NOT NULL,
    "RT/RW"                 VARCHAR(10) NOT NULL,
    nomor_telepon           VARCHAR(15) NOT NULL 
);

CREATE UNIQUE INDEX distribusi_zakat__idx ON
    distribusi_zakat (
        id_penerima_zakat
    ASC );

ALTER TABLE penerima_zakat ADD CONSTRAINT penerima_zakat_pk PRIMARY KEY ( id_penerima_zakat );

CREATE TABLE status_distribusi (
    id_status_distribusi   INTEGER NOT NULL,
    nama_status_distribusi VARCHAR(50) NOT NULL
);

ALTER TABLE status_distribusi ADD CONSTRAINT status_distribusi_pk PRIMARY KEY ( id_status_distribusi );

CREATE TABLE status_pembayaran_zakat (
    id_status_pembayaran_zakat INTEGER NOT NULL,
    nama_pembayaran_zakat      VARCHAR(50) NOT NULL
);

ALTER TABLE status_pembayaran_zakat ADD CONSTRAINT status_pembayaran_zakat_pk PRIMARY KEY ( id_status_pembayaran_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_amil_zakat_fk FOREIGN KEY ( id_amil_zakat )
        REFERENCES amil_zakat ( id_amil_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_bentuk_zakat_fk FOREIGN KEY ( id_bentuk_zakat )
        REFERENCES bentuk_zakat ( id_bentuk_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_status_distribusi_fk FOREIGN KEY ( id_status_distribusi )
        REFERENCES status_distribusi ( id_status_distribusi );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_amil_zakat_fk FOREIGN KEY ( id_amil_zakat )
        REFERENCES amil_zakat ( id_amil_zakat );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_bentuk_zakat_fk FOREIGN KEY ( id_bentuk_zakat )
        REFERENCES bentuk_zakat ( id_bentuk_zakat );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_jenis_zakat_fk FOREIGN KEY ( id_jenis_zakat )
        REFERENCES jenis_zakat ( id_jenis_zakat );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_pemberi_zakat_fk FOREIGN KEY ( id_pemberi_zakat )
        REFERENCES pemberi_zakat ( id_pemberi_zakat );

ALTER TABLE pemberi_zakat
    ADD CONSTRAINT pemberi_zakat_status_pembayaran_zakat_fk FOREIGN KEY ( id_status_pembayaran_zakat )
        REFERENCES status_pembayaran_zakat ( id_status_pembayaran_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_penerima_zakat_fk FOREIGN KEY ( id_penerima_zakat )
        REFERENCES penerima_zakat ( id_penerima_zakat );

INSERT INTO status_pembayaran_zakat (id_status_pembayaran_zakat, nama_pembayaran_zakat) values
(1, 'Sudah Membayar'),
(2, 'Belum Membayar')

INSERT INTO status_distribusi (id_status_distribusi, nama_status_distribusi) values 
(0, 'Tidak Ada Keterangan'),
(1, 'Telah Diberikan'),
(2, 'Belum Diberikan')

INSERT INTO jenis_zakat (id_jenis_zakat, nama_jenis_zakat) values 
(1, 'Zakat Fitrah'),
(2, 'Zakat Mal')

INSERT INTO bentuk_zakat (id_bentuk_zakat, nama_bentuk_zakat) values 
(1, 'Uang'),
(2, 'Beras'),
(3, 'Emas')

INSERT INTO amil_zakat (nama_amil_zakat, nik, alamat, "RT/RW", nomor_telepon) values
('Reza Thoriqis Sulthon', '3509065508124739', 'Jl Letjen Panjaitan No.30', '03/20', '082123456789'),
('Ade Kurniawan', '3917548206530905', 'Jl Trunoyojo VII/III Linkungan Sawahan Cantikan', '03/20', '085712345678'),
('Budi Wijaya', '3501974286503914', 'Jl. Merdeka No. 10, Kelurahan Gambir', '04/20', '081234567890'),
('Cahaya Kusuma', '3508416279530684', 'Jl. Kenanga No. 15, Kelurahan Sunter Jaya', '04/17', '082156789012')

INSERT INTO pemberi_zakat (nama_pemberi_zakat, nik, alamat, "RT/RW", nomor_telepon, id_status_pembayaran_zakat) values
('Fajar Hidayat', '3509724186530729', 'Jl. Trunojoyo VII No. 31', '03/20', '082267890123', 1),
('Indah Permata Sari', '3502894716503928', 'Jl. Trunojoyo VII No. 47', '03/20', '082378901234', 1),
('Joko Susilo', '3504719286530741', 'Jl. Trunojoyo VII No. 101', '03/20','085189012345', 2),
('Mila Setiawan', '3506184927530816', 'Jl. Trunojoyo VII No. 88', '03/20', '085290123456', 1)

INSERT INTO pembayaran_zakat (besar_pemberian, tanggal_pemberian, id_amil_zakat, id_pemberi_zakat, id_bentuk_zakat, id_jenis_zakat) values
(3, '12-10-2024', 1, 1, 2, 1),
(50000, '7-10-2024', 2, 3, 1, 2)

INSERT INTO penerima_zakat (nama_kepala_keluarga, No_KK, alamat, "RT/RW", nomor_telepon) values
('Putu Adi', '3509064281350697', 'Jl. Trunojoyo VII No. 17', '03/20', '088145678901'),
('Rina Wulandari', '3509061742385069', 'Jl. Trunojoyo VII No. 25', '03/20', '0882-5678-9012')

INSERT INTO distribusi_zakat (jumlah_paket_zakat, id_amil_zakat, id_bentuk_zakat, id_status_distribusi, id_penerima_zakat) values
(3, 1, 2, 0, 1),
(3, 1, 3, 0, 2)