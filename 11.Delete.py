import sqlite3
koneksi = sqlite3.connect('databese_fauna.db')
kursor = koneksi.cursor()

# ubah berdasarkan id_pegawai
asal = "Kalimantan"  # ID Fauna yang akan dihapus
kursor.execute(f"DELETE FROM FAUNA WHERE asal = ?", (asal,))
koneksi.commit()

# cek apakah data berrhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tdk
    print(f"Data Fauna Asal {asal} berhasil Dihapus!")
else:
    print(f"Tidak ada data Asal dengan Asal {asal}!")

# putuskan koneksi
koneksi.close()