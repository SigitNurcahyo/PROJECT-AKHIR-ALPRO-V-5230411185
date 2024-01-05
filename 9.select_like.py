# QUARY LIKE
import sqlite3
koneksi = sqlite3.connect('databese_fauna.db')
kursor = koneksi.cursor()
        
# menjalankan quary select dengan LIKE
# misalkan kita ingin mencari nama dengan awalan huruf D
nama_fauna = 'B%'
kursor.execute(f"SELECT * FROM FAUNA WHERE nama_fauna LIKE ?",(nama_fauna,))
baris_table = kursor.fetchall()
# Membuat format table dengan method format()
print("Data Fauna")
print("="*110)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID","nama_fauna","jenis","asal","jumlah_sekarang","tahun_ditemukan"))
print("_"*110)

#tampilkan data sesuai format tabel dg perulangan
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
koneksi.close()
