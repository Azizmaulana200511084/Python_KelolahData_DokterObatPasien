from db import DBConnection as mydb
class Dokter:
    def __init__(self):
        self.__iddokter= None
        self.__nip= None
        self.__nama_lengkap= None
        self.__spesialis= None
        self.__tempat_praktek= None
        self.conn= None
        self.affected= None
        self.result= None
    @property
    def iddokter(self):
        return self.__iddokter
    
    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap

    @nama_lengkap.setter
    def nama_lengkap(self, value):
        self.__nama_lengkap = value

    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value

    @property
    def tempat_praktek(self):
        return self.__tempat_praktek

    @tempat_praktek.setter
    def tempat_praktek(self, value):
        self.__tempat_praktek = value

    def simpan(self):
        self.conn= mydb()
        val = (self.__nip,self.__nama_lengkap,self.__spesialis,self.__tempat_praktek)
        sql = "INSERT INTO dokter (nip,nama_lengkap,spesialis,tempat_praktek) VALUES" + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip,self.__nama_lengkap,self.__spesialis,self.__tempat_praktek, id)
        sql = "UPDATE dokter SET nip=%s nama_lengkap=%s, spesialis=%s, tempat_praktek=%s WHERE iddokter=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama_lengkap,self.__spesialis,self.__tempat_praktek, nip)
        sql = "UPDATE dokter SET nama_lengkap=%s, spesialis=%s, tempat_praktek=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM dokter WHERE iddokter='"+ str(id) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql = "DELETE FROM dokter WHERE nip='"+ str(nip) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM dokter WHERE iddokter='"+ str(id) +"'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama_lengkap = self.result[2]
        self.__spesialis = self.result[3]
        self.__tempat_praktek = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM dokter WHERE nip='"+ b +"'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama_lengkap = self.result[2]
            self.__spesialis = self.result[3]
            self.__tempat_praktek = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama_lengkap = ''
            self.__spesialis = ''
            self.__tempat_praktek = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM dokter"
        self.result = self.conn.findAll(sql)
        return self.result

dok = Dokter()