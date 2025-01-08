from db import DBConnection as mydb
class Pasien:
    def __init__(self):
        self.__idpasien= None
        self.__nomor_pasien= None
        self.__nama_lengkap= None
        self.__jenis_kelamin= None
        self.__umur= None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idpasien(self):
        return self.__idpasien

    @property
    def nomor_pasien(self):
        return self.__nomor_pasien

    @nomor_pasien.setter
    def nomor_pasien(self, value):
        self.__nomor_pasien = value

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap

    @nama_lengkap.setter
    def nama_lengkap(self, value):
        self.__nama_lengkap = value

    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin

    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_pasien,self.__nama_lengkap,self.__jenis_kelamin,self.__umur)
        sql="INSERT INTO pasien (nomor_pasien,nama_lengkap,jenis_kelamin,umur) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_pasien,self.__nama_lengkap,self.__jenis_kelamin,self.__umur, id)
        sql="UPDATE pasien SET nomor_pasien=%s, nama_lengkap=%s, jenis_kelamin=%s, umur=%s WHERE idpasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nomor_pasien):
        self.conn = mydb()
        val = (self.__nama_lengkap,self.__jenis_kelamin,self.__umur, nomor_pasien)
        sql="UPDATE pasien SET nama_lengkap=%s, jenis_kelamin=%s, umur=%s WHERE nomor_pasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pasien WHERE idpasien='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nomor_pasien):
        self.conn = mydb()
        sql="DELETE FROM pasien WHERE nomor_pasien='" + str(nomor_pasien) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pasien WHERE idpasien='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_pasien = self.result[1]
        self.__nama_lengkap = self.result[2]
        self.__jenis_kelamin = self.result[3]
        self.__umur = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nomor_pasien):
        a=str(nomor_pasien)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pasien WHERE nomor_pasien='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_pasien = self.result[1]
            self.__nama_lengkap = self.result[2]
            self.__jenis_kelamin = self.result[3]
            self.__umur = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_pasien = ''
            self.__nama_lengkap = ''
            self.__jenis_kelamin = ''
            self.__umur = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pasien"
        self.result = self.conn.findAll(sql)
        return self.result

psn = Pasien()

# Tampilkan semua data
result = psn.getAllData()
print(result)

# Entri data
'''psn.nomor_pasien = '001'
psn.nama_lengkap = 'Sudirja'
psn.jenis_kelamin = 1
psn.umur=5
hasil = psn.simpan()
print(hasil)'''

# Cari data
'''nomor_pasien = '001'
hasil = psn.getByNIM(nim)
print(hasil)'''

# Update Data
'''nim = '001'
psn.nama_lengkap = 'Angel'
psn.jenis_kelamin=3
psn.umur=6
hasil = psn.updateByNIM(nomor_pasien)
print(hasil)'''

# delete data
'''nomor_pasien = '001'
hasil = psn.deleteByNIM(nomor_pasien)
print(hasil)'''
