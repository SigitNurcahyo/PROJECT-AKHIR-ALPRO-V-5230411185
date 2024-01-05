import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('databese_fauna.db')
kursor = koneksi.cursor()

# Data yang ingin diubah
id_fauna = 4

# Menjalankan query UPDATE
kursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur' WHERE id_fauna = {id_fauna}")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data Fauna {id_fauna} berhasil diupdate.")
else:
    print(f"Tidak ada data Fauna dengan ID {id_fauna}.")

# Menutup koneksi
koneksi.close()