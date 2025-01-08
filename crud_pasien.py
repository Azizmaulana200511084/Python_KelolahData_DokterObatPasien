from pasien import Pasien

def Tampil():
    psn = Pasien()
    result = psn.getAllData()
    for x in result:
        print(x)
    #Menupasien()

def Entry():
    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien: ")
    nama_lengkap = input("Masukkan nama lengkap pasien: ")
    jenis_kelamin = input("Masukkan jenis kelamin pasien: ")
    umur = input("Masukkan umur pasien: ")
    psn.nomor_pasien = nomor_pasien
    psn.nama_lengkap = nama_lengkap
    psn.jenis_kelamin = jenis_kelamin
    psn.umur = umur
    hasil = psn.simpan()
    if (hasil==1):
        print("Entry Data Berhasil!")
    else:
        print("Entry Data Gagal...")
    Menupasien()
    
def Cari():
    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Dicari: ")
    hasil = psn.getByNIM(nomor_pasien)
    print(hasil)
    Menupasien()
    
def Ubah():
    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Akan Diubah: ")
    hasil = psn.getByNIM(nomor_pasien)
    print("Data yang Ditemukan Sebagai Berikut:")
    print(hasil)
    print("Silahkan Lengkapi Data Berikut Untuk Mengganti:")
    nama_lengkap = input("Masukkan nama lengkap pasien: ")
    jenis_kelamin = input("Masukkan jenis kelamin pasien: ")
    umur = input("Masukkan umur pasien : ")
    psn.nomor_pasien = nomor_pasien
    psn.nama_lengkap = nama_lengkap
    psn.jenis_kelamin = jenis_kelamin
    psn.umur = int(umur)
    hasil = psn.updateByNIM(nomor_pasien)
    if(hasil==1):
        print("Data Berhasil Diubah!")
    else:
        print("Data Gagal Diubah...")
    Menupasien()
    
def Hapus():
    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Akan Dihapus: ")
    hasil = psn.getByNIM(nomor_pasien)
    print("Data yang Ditemukan Sebagai Berikut:")
    print(hasil)
    jawab = input("Apakah Data Ini Akan Dihapus (y/t)?:")
    if(jawab=="y"):
        hasil = psn.deleteByNIM(nomor_pasien)
        if(hasil==1):
            print("Data Berhasil Dihapus!")
        else:
            print("Data Gagal Dihapus...")
    else:
        print("Data Batal Untuk Dihapus.")

def Menupasien():
    lanjut = True
    while lanjut:
        print("\n\n                         _________________________________________\n                         |====  KELOLAH DATA PASIEN PGSQL ====|\n                         |Oleh: AZIZ MAULANA / 200511084 / R4    |\n                         |---------------------------------------|\n                         |                  Menu                 |\n                         |_______________________________________|\n                         | 1.| Lihat Data Pasien   _+++_   /p |\n                         | 2.| Tambah Data Pasien (^ _ ^) / O |\n                         | 3.| Cari Data Pasien  /|CRUUD|/  S |\n                         | 4.| Ubah Data Pasien  \|_____|   T |\n                         | 5.| Hapus Data Pasien   / |\ \   G |\n                         | 6.| Keluar               (__/  \__) R |\n                         |___|_________________________________E_|")
        p = int(input("                         PILIH MENU >>>"))
        print("\n\n")
        if(p==1):
            Tampil()
        elif(p==2):
            Entry()
        elif(p==3):
            Cari()
        elif(p==4):
            Ubah()
        elif(p==5):
            Hapus()
        elif(p==6):
            lanjut = False
            break
        else:
            lanjut = False
            break

Menupasien()

