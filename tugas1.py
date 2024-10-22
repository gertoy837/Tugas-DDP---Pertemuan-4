'''
TUGAS 1 INPUT OUTPUT & FORMAT PRINT
===================================
PT. XYZ memiliki sistem penggajian dengan data sbb (input):
nama pegawai, divisi, agama, jabatan.
Carilah data2 di bawah ini menggunakan struktur kendali IF:
- gaji pokok: jika jabatan staff = 4jt, kabag = 7jt, manager = 10jt
- tunjab = 20% dari gapok
- gaji kotor = gaji pokok + tunjab
- zakat 2,5 % dari gaji kotor(gunakan ternary) =
  jika muslim dan gaji kotor minimal 7jt
- gaji bersih = (gapok + tunjab) - zakat

Cetaklah data2 di atas dengan format print sesuai tipe data masing2:
Nama                :
Agama               :
Divisi              :
Jabatan             :
Gaji Pokok          :
Tunjangan Jabatan   :
Gaji Kotor          :
Zakat Profesi       :
Gaji Bersih         :

Kirim 1 pekan setelah materi ke email asdos masing2
subject: DDP_tugas1_NIM_NAMA_Rombel
'''
print("+==========================================================+")
print("|                  Data Penggajian PT. XYZ                 |")
print("+==========================================================+")

nama = str(input("Masukkan Nama Pegawai: ").lower())
divisi = str(input("Masukkan Divisi: ").lower())
agama = str(input("Masukkan Agama: ").lower())
jabatan = str(input("Masukkan Jabatan: ").lower())

if (jabatan == "staff"):
  gaji_pokok = 4000000
elif (jabatan == "kabag"):
  gaji_pokok = 7000000
elif (jabatan == "manager"):
  gaji_pokok = 10000000
else:
  print("Jabatan yang Anda masukkan salah!")
  exit()

tunjab = 0.20 * gaji_pokok

gaji_kotor = gaji_pokok + tunjab

zakat = 0.025 * gaji_kotor if (agama == "muslim" or agama == "islam" and gaji_kotor >= 7000000) else 0

gaji_bersih = gaji_pokok + tunjab - zakat

print("+==========================================================+")
print("|                  Data Penggajian PT. XYZ                 |")
print("+==========================================================+")
# print(f"Nama\t\t\t: {nama.title()} \nAgama\t\t\t: {agama.title()} \nDivisi\t\t\t: {divisi.title()} \nJabatan\t\t\t: {jabatan.title()} \nGaji Pokok\t\t: {gaji_pokok} \nTunjangan Jabatan\t: {tunjab} \nGaji Kotor\t\t: {gaji_kotor} \nZakat Profesi\t\t: {zakat} \nGaji Bersih\t\t: {gaji_bersih}")

# print("Nama\t\t\t: %s"
#       "\nAgama\t\t\t: %s"
#       "\nDivisi\t\t\t: %s"
#       "\nJabatan\t\t\t: %s"
#       "\nGaji Pokok\t\t: Rp. %.2f"
#       "\nTunjangan Jabatan\t: Rp. %.2f"
#       "\nGaji Kotor\t\t: Rp. %.2f"
#       "\nZakat Profesi\t\t: Rp. %.2f"
#       "\nGaji Bersih\t\t: Rp. %.2f" %(nama.title(),agama.title(),divisi.title(),jabatan.title(),gaji_pokok,tunjab,gaji_kotor,zakat,gaji_bersih))

print("Nama                :", nama.title())
print("Agama               :", agama.title())
print("Divisi              :", divisi.title())
print("Jabatan             :", jabatan.title())
print(f"Gaji Pokok          : Rp. {gaji_pokok:,.2f}")
print(f"Tunjangan Jabatan   : Rp. {tunjab:,.2f}")
print(f"Gaji Kotor          : Rp. {gaji_kotor:,.2f}")
print(f"Zakat Profesi       : Rp. {zakat:,.2f}")
print(f"Gaji Bersih         : Rp. {gaji_bersih:,.2f}")
