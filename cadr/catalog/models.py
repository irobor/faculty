from .. import sqlalchm
from .. import mysql


myslbd = mysql
class Tester(sqlalchm.Model):
    __tablename__ = 'tester'
    id = sqlalchm.Column(sqlalchm.Integer, primary_key=True)
    title = sqlalchm.Column(sqlalchm.String(80))
    position = sqlalchm.Column(sqlalchm.Integer)
    menu_name = sqlalchm.Column(sqlalchm.Text, nullable=False)


class MsqlCatalog:

    def classes_select(self):  # все классы classes
        with mysql.connection.cursor() as cours:
            query = "SELECT * FROM classes"
            cours.execute(query)
            result = cours.fetchall()
        return result

    def classes_uniq_select(self, url):  # выбираем класс где url = входящей переменной
        with mysql.connection.cursor() as cours:
            query = "SELECT * FROM classes WHERE url = %s"
            cours.execute(query, (url,))
            result = cours.fetchone()
        return result

    def courses(self):  # все курсы
        with mysql.connection.cursor() as cours:
            query = '''
            SELECT courses.*, category_cours.name as cat_name
            FROM courses 
            LEFT JOIN category_cours 
            ON courses.id_category = category_cours.id
            '''
            cours.execute(query)
            result = cours.fetchall()
        return result

    def category(self):  # все категории
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM category_cours"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def category_uniq(self, id):  # выбираем уникальную категорию
        with mysql.connection.cursor() as cat:
            query = "SELECT * FROM category_cours WHERE id = %s"
            cat.execute(query, (id,))
            result = cat.fetchone()
        return result

    def coursses_id_category(self, id):  # выбираем курсы где id_category = переменной
        with mysql.connection.cursor() as cur:
            query = '''
            SELECT courses.*, category_cours.name as cat_name
            FROM courses 
            LEFT JOIN category_cours 
            ON courses.id_category = category_cours.id
            WHERE courses.id_category = %s AND courses.visible = '1'
            '''
            cur.execute(query, (id,))
            result = cur.fetchall()
        return result

    def one_course(self, id):  # выбираем уникальный курс где id = переменной WHERE visible = '1'
        with mysql.connection.cursor() as cur:
            query = ''' 
            SELECT 
                courses.*, 
                format_learning.name as format
            FROM 
                courses
            JOIN 
                format_learning 
            ON 
                courses.id_format_learning = format_learning.id
            WHERE 
                courses.id  = %s 
            '''
            cur.execute(query, (id,))
            result = cur.fetchone()
        return result

    def modul_course(self, id):  # выбираем уникальный модуль курса где id = переменной
        with mysql.connection.cursor() as modl:
            query = "SELECT * FROM modul_course_%s"
            modl.execute(query, (id,))
            result = modl.fetchall()
        return result

    def price_course(self, id):  # выбираем цену и часы для каждого курса отдельно где id = id курса
        with mysql.connection.cursor() as modl:
            query = '''
            SELECT name.name AS name, price.price AS price, price.watch AS watch, price.watch_word AS word
            FROM price_certificat AS price
            LEFT JOIN name_price AS name
            ON price.id_price_name = name.id 
            WHERE price.id_classes = %s
            '''
            modl.execute(query, (id,))
            result = modl.fetchall()
        return result

    def certification_jpg(self, id):  # выбираем url образцов удостоверений .jpg
        with mysql.connection.cursor() as modl:
            query = '''
            SELECT file.name AS url
            FROM download_file_classes AS dwnld
            LEFT JOIN file_certification AS file
            ON dwnld.id_file = file.id 
            WHERE dwnld.id_classes = %s
            '''
            modl.execute(query, (id,))
            result = modl.fetchall()
        return result

    def price_course_all(self):  # выбираем цену и часы для всех курсов (не применяется)
        with mysql.connection.cursor() as modl:
            query = '''
            SELECT name.name AS name, price.id_classes AS id, price.price AS price, price.watch AS watch, price.watch_word AS word
            FROM price_certificat AS price
            LEFT JOIN name_price AS name
            ON price.id_price_name = name.id
            '''
            modl.execute(query)
            result = modl.fetchall()
        return result

    def popular_course_all(self):  # выбираем популярные курсы для каталога
        with mysql.connection.cursor() as modl:
            query = '''
            SELECT cat.name AS cat_curs, courses.name AS name, tr.id_course AS id_cours, courses.price AS price, count(*) AS counts
            FROM transaction_course tr
            JOIN courses 
                ON courses.id = tr.id_course
            JOIN category_cours AS cat
                ON cat.id = courses.id_category
            WHERE courses.visible = 1
            GROUP BY id_cours
            ORDER BY counts DESC
            '''
            modl.execute(query)
            result = modl.fetchall()
        return result

    def doc_pdf(self, id):  # выбираем url для программы ДПО .pdf
        with mysql.connection.cursor() as modl:
            query = '''
            SELECT file.name AS url
            FROM doc_dpo_course AS dwnld
            LEFT JOIN doc_dpo_files AS file
            ON dwnld.id_doc_dpo = file.id 
            WHERE dwnld.id_course = %s
            '''
            modl.execute(query, (id,))
            result = modl.fetchone()
        return result
