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
    id_amil_zakat           INTEGER NOT NULL,
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

CREATE TABLE detail_distribusi_zakat (
    id_detail_distribusi                 SERIAL NOT NULL,
    jumlah_zakat                         INTEGER NOT NULL, 
    id_distribusi_zakat                  INTEGER NOT NULL,
    id_bentuk_zakat         INTEGER NOT NULL,
);

ALTER TABLE detail_distribusi_zakat ADD CONSTRAINT detail_distribusi_zakat_pk PRIMARY KEY ( id_detail_distribusi );

ALTER TABLE detail_distribusi_zakat
    ADD CONSTRAINT detail_distribusi_zakat_bentuk_zakat_fk FOREIGN KEY ( id_bentuk_zakat )
        REFERENCES bentuk_zakat ( id_bentuk_zakat );

ALTER TABLE detail_distribusi_zakat
    ADD CONSTRAINT detail_distribusi_zakat_distribusi_zakat_fk FOREIGN KEY ( id_distribusi_zakat )
        REFERENCES distribusi_zakat ( id_distribusi_zakat ) ON DELETE CASCADE;

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_amil_zakat_fk FOREIGN KEY ( id_amil_zakat )
        REFERENCES amil_zakat ( id_amil_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_status_distribusi_fk FOREIGN KEY ( id_status_distribusi )
        REFERENCES status_distribusi ( id_status_distribusi );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_amil_zakat_fk FOREIGN KEY ( id_amil_zakat )
        REFERENCES amil_zakat ( id_amil_zakat ) ON DELETE CASCADE;

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_bentuk_zakat_fk FOREIGN KEY ( id_bentuk_zakat )
        REFERENCES bentuk_zakat ( id_bentuk_zakat );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_jenis_zakat_fk FOREIGN KEY ( id_jenis_zakat )
        REFERENCES jenis_zakat ( id_jenis_zakat );

ALTER TABLE pembayaran_zakat
    ADD CONSTRAINT pembayaran_zakat_pemberi_zakat_fk FOREIGN KEY ( id_pemberi_zakat )
        REFERENCES pemberi_zakat ( id_pemberi_zakat ) ON DELETE CASCADE;

ALTER TABLE pemberi_zakat
    ADD CONSTRAINT pemberi_zakat_status_pembayaran_zakat_fk FOREIGN KEY ( id_status_pembayaran_zakat )
        REFERENCES status_pembayaran_zakat ( id_status_pembayaran_zakat );

ALTER TABLE distribusi_zakat
    ADD CONSTRAINT distribusi_zakat_penerima_zakat_fk FOREIGN KEY ( id_penerima_zakat )
        REFERENCES penerima_zakat ( id_penerima_zakat ) ON DELETE CASCADE;

INSERT INTO status_pembayaran_zakat (id_status_pembayaran_zakat, nama_pembayaran_zakat) values
(1, 'Sudah Membayar'),
(2, 'Belum Membayar')

INSERT INTO status_distribusi (id_status_distribusi, nama_status_distribusi) values 
(1, 'Telah Diberikan'),
(2, 'Belum Diberikan')

INSERT INTO jenis_zakat (id_jenis_zakat, nama_jenis_zakat) values 
(1, 'Zakat Fitrah'),
(2, 'Zakat Mal')

INSERT INTO bentuk_zakat (id_bentuk_zakat, nama_bentuk_zakat) values 
(1, 'Beras'),
(2, 'Uang'),
(3, 'Emas')

INSERT INTO amil_zakat (nama_amil_zakat, nik, alamat, "RT/RW", nomor_telepon) VALUES
('Reza Thoriqis Sulthon', '3509065508124739', 'Jl Letjen Panjaitan No.30', '03/20', '082123456789'),
('Ade Kurniawan', '3917548206530905', 'Jl Trunoyojo VII/III Linkungan Sawahan Cantikan', '03/20', '085712345678'),
('Ahmad Fauzi', '3501234567890123', 'Jl. Trunojoyo No.10', '01/20', '089123456789'),
('Budi Prasetyo', '3502345678901234', 'Jl. Trunojoyo No.12', '01/20', '081234567890'),
('Chandra Wijaya', '3503456789012345', 'Jl. Trunojoyo No.14', '02/20', '085234567890'),
('Dian Permata', '3504567890123456', 'Jl. Trunojoyo No.16', '02/20', '089234567891'),
('Eka Sari', '3505678901234567', 'Jl. Trunojoyo No.18', '03/20', '081345678901'),
('Farid Santoso', '3506789012345678', 'Jl. Trunojoyo No.20', '03/20', '085345678902'),
('Gita Mawarni', '3507890123456789', 'Jl. Trunojoyo No.22', '01/20', '089456789012');

INSERT INTO pemberi_zakat (nama_pemberi_zakat, nik, alamat, "RT/RW", nomor_telepon, id_status_pembayaran_zakat) VALUES
('Reza Thoriqis Sulthon', '3509065508124739', 'Jl Letjen Panjaitan No.30', '03/20', '082123456789', 2),
('Ade Kurniawan', '3917548206530905', 'Jl Trunoyojo VII/III Linkungan Sawahan Cantikan', '03/20', '085712345678', 2),
('Budi Santoso', '3501234567890123', 'Jl. Trunojoyo No.10', '01/20', '089123456789', 2),
('Siti Aminah', '3502345678901234', 'Jl. Trunojoyo No.12', '01/20', '081234567890', 2),
('Joko Widodo', '3503456789012345', 'Jl. Trunojoyo No.14', '02/20', '085234567890', 2),
('Ani Yudhoyono', '3504567890123456', 'Jl. Trunojoyo No.16', '02/20', '089234567891', 2),
('Ratna Dewi', '3505678901234567', 'Jl. Trunojoyo No.18', '03/20', '081345678901', 2),
('Taufik Hidayat', '3506789012345678', 'Jl. Trunojoyo No.20', '03/20', '085345678902', 2),
('Andi Lala', '3507890123456789', 'Jl. Trunojoyo No.22', '01/20', '089456789012', 2),
('Dewi Sartika', '3508901234567890', 'Jl. Trunojoyo No.24', '01/20', '081456789012', 2),
('Fajar Nugroho', '3509012345678901', 'Jl. Trunojoyo No.26', '02/20', '085456789012', 2),
('Gina Indah', '3500123456789012', 'Jl. Trunojoyo No.28', '02/20', '089567890123', 2),
('Hendra Kurniawan', '3501234567890234', 'Jl. Trunojoyo No.30', '03/20', '081567890123', 2),
('Ika Sari', '3502345678902345', 'Jl. Trunojoyo No.32', '03/20', '085567890123', 2),
('Johan Setiawan', '3503456789012456', 'Jl. Trunojoyo No.34', '01/20', '089678901234', 2),
('Kiki Amelia', '3504567890123457', 'Jl. Trunojoyo No.36', '01/20', '081678901234', 2),
('Lukman Hakim', '3505678901234568', 'Jl. Trunojoyo No.38', '02/20', '085678901234', 2),
('Maya Anggraini', '3506789012345679', 'Jl. Trunojoyo No.40', '02/20', '089789012345', 2),
('Nina Putri', '3507890123456780', 'Jl. Trunojoyo No.42', '03/20', '081789012345', 2),
('Oki Setiana', '3508901234567891', 'Jl. Trunojoyo No.44', '03/20', '085789012345', 2),
('Pandu Aditya', '3509012345678902', 'Jl. Trunojoyo No.46', '01/20', '089890123456', 2),
('Qory Sandioriva', '3500123456789013', 'Jl. Trunojoyo No.48', '01/20', '081890123456', 2);

INSERT INTO penerima_zakat (nama_kepala_keluarga, No_KK, alamat, "RT/RW", nomor_telepon) VALUES
('Fajar Nugroho', '3501234567890123', 'Jl. Trunojoyo No.10', '01/20', '089123456789'),
('Ratna Dewi', '3502345678901234', 'Jl. Trunojoyo No.12', '01/20', '081234567890'),
('Taufik Hidayat', '3503456789012345', 'Jl. Trunojoyo No.14', '02/20', '085234567890'),
('Andi Lala', '3504567890123456', 'Jl. Trunojoyo No.16', '02/20', '089234567891'),
('Johan Setiawan', '3505678901234567', 'Jl. Trunojoyo No.18', '03/20', '081345678901'),
('Joko Widodo', '3506789012345678', 'Jl. Trunojoyo No.20', '03/20', '085345678902'),
('Lukman Hakim', '3507890123456789', 'Jl. Trunojoyo No.22', '01/20', '089456789012'),
('Hendra Kurniawan', '3508901234567890', 'Jl. Trunojoyo No.24', '01/20', '081456789012'),
('Oki Setiana', '3509012345678901', 'Jl. Trunojoyo No.26', '02/20', '085456789012'),
('Pandu Aditya', '3500123456789012', 'Jl. Trunojoyo No.28', '02/20', '089567890123'),
