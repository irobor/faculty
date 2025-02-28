from .. import mysql

class MsqlWidgets:
    def classes_select(self):  # все классы classes Квалификация, Переподготовка
        with mysql.connection.cursor() as cours:
            query = "SELECT * FROM classes WHERE visible = '1' ORDER BY position"
            cours.execute(query)
            result = cours.fetchall()
        return result

    def category(self):  # все категории
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM category_cours WHERE visible = '1'"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def menu(self):  # главное меню сайта
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM menu WHERE visible = '1' ORDER BY position"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def sub_menu(self):  # drop menu сайта
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM sub_menu"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def sub_menu_id_menu(self, id_menu):  # sub menu ГДЕ id-menu 
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM sub_menu WHERE id_menu = %s"
            cur.execute(query, (id_menu,))
            result = cur.fetchall()
        return result

    def service_license(self):  # sub menu услуги лицензии
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM service_license"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def service_sro(self):  # sub menu услуги СРО
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM service_sro"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def service_certificates(self):  # sub menu Услуги Сертификаты
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM service_certificates"
            cur.execute(query)
            result = cur.fetchall()
        return result

    def attestation(self):  # получаем все аттестации
        with mysql.connection.cursor() as cur:
            query = "SELECT * FROM attestation"
            cur.execute(query)
            result = cur.fetchall()
        return result
 