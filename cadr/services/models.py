from .. import sqlalchm
from .. import mysql

myslbd = mysql

class MsqlServices():
    

    def license_all(self):# все лицензии license
        cours = myslbd.connection.cursor()
        cours.execute('''SELECT * FROM service_license''')
        return cours.fetchall()

    def license_one(self, name):
        cur = myslbd.connection.cursor()
        cur.execute('''SELECT * FROM service_license WHERE url = '%s' '''% (name))
        return cur.fetchone()

    def sro_all(self):# все лицензии license
        cours = myslbd.connection.cursor()
        cours.execute('''SELECT * FROM service_sro''')
        return cours.fetchall()    

    def sro_one(self, name):
        cur = myslbd.connection.cursor()
        cur.execute('''SELECT * FROM service_sro WHERE url = '%s' '''% (name))
        return cur.fetchone()

    def certificate_all(self):# все лицензии license
        cours = myslbd.connection.cursor()
        cours.execute('''SELECT * FROM service_certificates''')
        return cours.fetchall()    

    def certificate_one(self, name):
        cur = myslbd.connection.cursor()
        cur.execute('''SELECT * FROM service_certificates WHERE url = '%s' '''% (name))
        return cur.fetchone() 

    def doc_license(self, cat, url_license):# документы для полчения лицензии
        cur = myslbd.connection.cursor()
        cur.execute(f"SELECT * FROM doc_license WHERE name_cat = '%s' AND url_license = '%s' "% (cat, url_license))
        return cur.fetchone()              

