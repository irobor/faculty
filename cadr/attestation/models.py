from .. import sqlalchm
from .. import mysql

myslbd = mysql

class MsqlAttestation():

    def attest_all(self):# все аттестации
        attest = myslbd.connection.cursor()
        attest.execute(f" SELECT * FROM attestation ")
        return attest.fetchall()

    def attest_one(self, url_id):# одна аттестация по url_id
        attest = myslbd.connection.cursor()
        attest.execute(f" SELECT * FROM attestation WHERE url_id = '%s' " %(url_id))
        return attest.fetchone()  

    # таблица аттестации по переменной id_att
    def attest_table(self, id_att):
        attest = myslbd.connection.cursor()
        attest.execute(f" SELECT * FROM attestation_table WHERE id_att = '%s' " %(id_att))
        return attest.fetchall()
        
    # Получаем имя файла заявки для скачивания url
    def download_file(self, id_url):
        attest = myslbd.connection.cursor()
        attest.execute(f" SELECT fl.name FROM download_file AS dwn LEFT JOIN file_doc AS fl ON  fl.id = dwn.id_file WHERE  dwn.url_course = '%s' " %(id_url))
        return attest.fetchone()
        
    # Получаем url  img (образец удостоверения)
    def img_certificat(self, id_url):
        attest = myslbd.connection.cursor()
        attest.execute(f" SELECT fl.name as img FROM dwnld_certificat AS dwn LEFT JOIN file_certification AS fl ON  fl.id = dwn.id_file WHERE  dwn.url_course = '%s' " %(id_url))
        return attest.fetchone()    