from obat import obat

def tampil():
   ob = obat()
   result = ob.getAllData()
   for i in result:
      print(i)
   Menu()

def entry():
   ob = obat()
   ko = input("Masukan Kode Obat: ")
   nama = input("Masukan Nama Obat: ")
   bt = input("Masukan Bentuk Obat: ")
   br = input("Masukan Berat Obat: ")   
   ob.kode_obat = int(ko)
   ob.nama_obat = nama
   ob.bentuk = bt
   ob.berat = br
   hasil = ob.simpan()
   if (hasil==1):
      print("Data Berhasil Disimpan")
   else:
      print("Data Gagal Disimpan!")
   Menu()

def cari():
   ob = obat()
   ko = input("Masukan Kode Obat: ")
   hasil = ob.getBykode_obat(ko)
   print(hasil)
   Menu()

def ubah():
   ob = obat()
   ko = input("Masukan Kode Obat: ")
   hasil = ob.getBykode_obat(ko)
   print("Data Berhasil Ditemukan!")
   print(hasil)
   print("Silahkan Lengkapi Data Berikut Untuk MengUpdate:")
   nama = input("Masukan Nama Obat: ")
   bt = input("Masukan Bentuk Obat: ")
   br = input("Masukan Berat Obat: ")   
   ob.kode_obat = int(ko)
   ob.nama_obat = nama
   ob.bentuk = bt
   ob.berat = br
   hasil = ob.updateBykode_obat(ko)
   if (hasil==1):
      print("Data Berhasil DiUpdate!")
      up = ob.getAllData()
      print("===========================")
      print("List Data Setelah DiUpdate!")
      for i in up:
         print(i)
   else:
      print("Data Gagal DiUpdate!")
   Menu()

def hapus():
   ob = obat()
   ko = input("Masukan Kode Obat: ")
   hasil = ob.getBykode_obat(ko)
   print("Data Berhasil Ditemukan!")
   print(hasil)
   jwb = input("Apakah data ini akan dihapus (y/t): ").lower()
   if (jwb == 'y'):
      hasil = ob.deleteBykode_obat(ko)
      if hasil == 1 :
         print("Data Berhasil Dihapus!")
         up = ob.getAllData()
         print("==========================")
         print("List Data Setelah Dihapus!")
         for i in up:
            print(i)
      else:
         print("Data Batal Dihapus!")
   else:
      print("Data Batal Dihapus!")
   Menu()

def Menu():
   lanjut = True
   while lanjut:
      print("\n\n                         _________________________________________\n                         |====  KELOLAH DATA OBAT PGSQL ====|\n                         |Oleh: AZIZ MAULANA / 200511084 / R4    |\n                         |---------------------------------------|\n                         |                  Menu                 |\n                         |_______________________________________|\n                         | 1.| Lihat Data Obat   _+++_   /p |\n                         | 2.| Tambah Data Obat (^ _ ^) / O |\n                         | 3.| Cari Data Obat  /|CRUUD|/  S |\n                         | 4.| Ubah Data Obat  \|_____|   T |\n                         | 5.| Hapus Data Obat   / |\ \   G |\n                         | 6.| Keluar               (__/  \__) R |\n                         |___|_________________________________E_|")
      p = int(input("                         PILIH MENU >>>"))
      if p == 1:
         tampil()
      elif p == 2:
         entry()
      elif p == 3:
         cari()
      elif p == 4:
         ubah()
      elif p == 5:
         hapus()
      elif p == 6:
         lanjut = False
         break
      else:
         lanjut = False
         break

Menu()