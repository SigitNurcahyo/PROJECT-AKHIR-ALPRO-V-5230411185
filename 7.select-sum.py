import sqlite3
koneksi = sqlite3.connect('databese_fauna.db')
kursor = koneksi.cursor()
# ambil data berdasarkan rata-rata gaji
#kursor.execute("SELECT AVG(jumlah_sekarang) FROM PEGAWAI") #rata rata gaji
kursor.execute("SELECT SUM(jumlah_sekarang) FROM FAUNA") #total fauna
total_populasi = kursor.fetchone()[0] # ambil data gaji jadikan baris baru dimulai dari indeks o
print(f"Total populasi fauna adalah:{total_populasi}")

koneksi.close()