from dokter import Dokter

def Tampil():
    dok = Dokter()
    result = dok.getAllData()
    for x in result:
        print("Data yang di tampilkan sebagai berikut:")
        print(x)
    MenuDokter()

def Cari():
    dok = Dokter()
    nip = input("Masukan NIP yang di cari:")
    hasil = dok.getByNIP(nip)
    print(hasil)
    MenuDokter()
    
def Entry():
    dok = Dokter()
    nip = input("Masukan NIP:")
    nama_lengkap = input("Masukan Nama Lengkap:")
    sp = input("Masukan Spesialis:")
    tp = input("Masukan Tempat Praktek:")
    dok.nip=nip
    dok.nama_lengkap=nama_lengkap
    dok.spesialis=sp
    dok.tempat_praktek=tp
    hasil = dok.simpan()
    if(hasil==1):
        print("Entry data berhasil")
    else:
        print("Enty data gagal.")
    MenuDokter()

    
def Ubah():
    dok = Dokter()
    nip = input("Masukan NIP yang akan di ubah:")
    hasil = dok.getByNIP(nip)
    print("Data yang di temukan sebagai berikut:")
    print(hasil)
    print("Silakan lengkapi data berikut untuk mengganti:")
    nama_lengkap = input("Masukan Nama Dokter:")
    sp = input("Masukan Spesialis:")
    tp = input("Masukan Tempat Praktek:")
    dok.nip=nip
    dok.nama_lengkap=nama_lengkap
    dok.spesialis=sp
    dok.tempat_praktek=tp
    hasil = dok.updateByNIP(nip)
    if(hasil==1):
        print("Data berhasil di ubah.")
    else:
        print("Data gagal di ubah.")
    MenuDokter()
    
def Hapus():
    dok = Dokter()
    nip = input("Masukan NIP yang akan dihapus:")
    hasil = dok.getByNIP(nip)
    print("Data yang ditemukan sebagai berikut:")
    print(hasil)
    jawab = input("Apakah data ini akan di hapus (y/t) ?")
    if(jawab=="y"):
        hasil = dok.deleteByNIP(nip)
        if(hasil==1):
            print("Data berhasil di hapus.")
        else:
            print("Data gagal di hapus.")
    else:
        print("Data batal untuk di hapus.")
    MenuDokter()
        
def MenuDokter():
    lanjut = True
    while lanjut:
        print("\n\n                         _________________________________________\n                         |====  KELOLAH DATA DOKTER PGSQL ====|\n                         |Oleh: AZIZ MAULANA / 200511084 / R4    |\n                         |---------------------------------------|\n                         |                  Menu                 |\n                         |_______________________________________|\n                         | 1.| Lihat Data Pasien   _+++_   /p |\n                         | 2.| Tambah Data Pasien (^ _ ^) / O |\n                         | 3.| Cari Data Pasien  /|CRUUD|/  S |\n                         | 4.| Ubah Data Pasien  \|_____|   T |\n                         | 5.| Hapus Data Pasien   / |\ \   G |\n                         | 6.| Keluar               (__/  \__) R |\n                         |___|_________________________________E_|")
        p = int(input("                         PILIH MENU >>>"))
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
MenuDokter()