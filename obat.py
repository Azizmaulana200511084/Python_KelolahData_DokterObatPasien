from db import DBConnection as mydb
class obat:
    def __init__(self):
        self.__idobat= None
        self.__kode_obat= None
        self.__nama_obat= None
        self.__bentuk= None
        self.__berat= None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idobat(self):
        return self.__idobat
    
    @property
    def kode_obat(self):
        return self.__kode_obat

    @kode_obat.setter
    def kode_obat(self, value):
        self.__kode_obat = value
    
    @property
    def nama_obat(self):
        return self.__nama_obat

    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value
    
    @property
    def bentuk(self):
        return self.__bentuk

    @bentuk.setter
    def bentuk(self, value):
        self.__bentuk = value
    
    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_obat,self.__nama_obat,self.__bentuk,self.__berat)
        sql="INSERT INTO obat (kode_obat,nama_obat,bentuk,berat) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_obat,self.__nama_obat,self.__bentuk,self.__berat, id)
        sql="UPDATE obat SET kode_obat=%s, nama_obat=%s, bentuk=%s, berat=%s WHERE idobat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBykode_obat(self, kode_obat):
        self.conn = mydb()
        val = (self.__nama_obat,self.__bentuk,self.__berat, kode_obat)
        sql="UPDATE obat SET nama_obat=%s, bentuk=%s, berat=%s WHERE kode_obat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE idobat='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBykode_obat(self, kode_obat):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE kode_obat='" + str(kode_obat) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE idobat='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_obat = self.result[1]                   
        self.__nama_obat = self.result[2]                   
        self.__bentuk = self.result[3]                   
        self.__berat = self.result[4]                   
        self.conn.disconnect
        return self.result
        
    def getBykode_obat(self, kode_obat):
        a=str(kode_obat)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE kode_obat='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_obat = self.result[1]
            self.__nama_obat = self.result[2]
            self.__bentuk = str(self.result[3])
            self.__berat = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_obat = ''                  
            self.__nama_obat = ''                  
            self.__bentuk = ''                  
            self.__berat = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result

mhs = obat() 

# Tampilkan semua data
result = mhs.getAllData()
print(result)

# Entri data
"""mhs.kode_obat = '6574'
mhs.nama_obat = 'Abbas'
mhs.bentuk = 1
mhs.berat=1
hasil = mhs.simpan()
print(hasil)
result = mhs.getAllData()
print(result)"""

# Cari data
'''kode_obat = '6574'
hasil = mhs.getBykode_obat(kode_obat)
print(hasil)'''

# Update Data
"""kode_obat = '6574'
mhs.nama_obat = 'Abbas Aziz'
mhs.bentuk=3
mhs.berat=2
hasil = mhs.updateBykode_obat(kode_obat)
print(hasil)"""

# delete data
"""kode_obat = '6574'
hasil = mhs.deleteBykode_obat(kode_obat)
print(hasil)"""