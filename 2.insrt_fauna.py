# import module
import sqlite3
# koneksi database
conn = sqlite3.connect('databese_fauna.db')

# list data faunan
nama_fauna =[
    ('Harimau jawa','Mamalia','Jawa','40','2019'),
    ('Kuskus Beruang','Mamalia','Sulawesi','30','2021'),
    ('Beruang Madu','Mamalia','Sumatera','1000','2020'),
    ('Pesut Mahakam','Mamalia','Kalimantan','100','2021'),
    ('Burung Maleo','Burung','Sulawesi','7000','2023'),
    ('Macan Dahan','Mamalia','Sumatrea','400','2020'),
    ('Kancil','Mamalia','Jawa','60','2022'),
    ('Gajah Kalimantan','Mamalia','Kalimantan','1500','2021'),
    ('Elang Jawa','Burung','Jawa','200','2021'),
    ('katak Borneo','Amfibi','Kalimantan','2000','2023'),
]
# variable insert SQL
insert_data = '''
             INSERT INTO FAUNA (nama_fauna, jenis, asal,jumlah_sekarang,tahun_ditemukan)
             VALUES (?,?,?,?,?)
'''
# execute insert data mahasiswa
conn.executemany(insert_data, nama_fauna)
conn.commit()
conn.close()