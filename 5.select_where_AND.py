import sqlite3
koneksi = sqlite3.connect('databese_fauna.db')
# SELECT ALL DATA PEGAWAI

kursor = koneksi.cursor()
# MENGAMBIL SEMUA DATA DALA TABEL DAN TAMPILKAN
kursor.execute("SELECT * FROM FAUNA WHERE jenis = 'Mamalia' AND jumlah_sekarang <= '1000'")
# Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

# Membuat format table dengan method format()
print("Data Fauna")
print("="*110)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","nama_fauna","jenis","asal","jumlah_sekarang","tahun_ditemukan"))
print("_"*110)

#tampilkan data sesuai format tabel dg perulangan
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
koneksi.close()