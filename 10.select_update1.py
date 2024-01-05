# update table_name
# set column1 =value1, colum2 =value2, ...
# Where condition:

import sqlite3
koneksi = sqlite3.connect('databese_fauna.db')
kursor = koneksi.cursor()

# ubah berdasarkan id_pegawai
id_fauna = 10
jumlah = 650

# gunakan Query UPDATE SET
kursor.execute(f"UPDATE FAUNA SET jumlah_sekarang = {jumlah} WHERE id_fauna = {id_fauna}")
koneksi.commit()

# cek apakah data berrhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tdk
    print(f"Data dengan ID {id_fauna} berhasil Diubah!")
else:
    print(f"Tidak ada data pegawai dengan ID {id_fauna}!")

# putuskan koneksi
koneksi.close()