from .. import sqlalchm
from .. import mysql


myslbd = mysql

class MsqlSearch():

    def search_courses(self, word):# поиск по ключевому слову, Таблица курсы
        cours = myslbd.connection.cursor()
        cours.execute("""SELECT courses.* , category_cours.title as cat_title 
                        FROM courses 
                        LEFT JOIN category_cours 
                        ON courses.id_category = category_cours.id
                        WHERE courses.id_category = category_cours.id AND courses.title like '%s' """% ('%'+word+'%'))
        return cours.fetchall()



        