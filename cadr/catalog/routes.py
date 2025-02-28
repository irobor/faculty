from flask import Blueprint, render_template, request
from .models import myslbd, Tester, MsqlCatalog
from ..widgets.breadcamp import Breadcamp #Хлебные крошки

catalog = Blueprint('catalog', __name__, url_prefix='/catalog', template_folder='templates')




@catalog.route('/')
def index():
    	# Генерируется своя индексная страница коталога
	title = 'Каталог курсов Повышения квалификации, Профессиональной Переподготовки, Рабочие специальности  | УЦ Факультет'
	description = 'Если вы не знаете, с чего начать или что изучать дальше, это отличное место для начала. Ознакомьтесь с нашими лучшими курсами для получения и развития нужных навыков и развития вашей карьеры.'
	model = MsqlCatalog()
	courses = model.courses()
    # Получаем массив цену и часы удостоверений.
	price_watch = model.price_course_all()
    #получаем популярные курсы
	popular_course_all = model.popular_course_all()
	sqlAlqTester = Tester.query.all()# это тестовая строчка		
	return render_template('catalog/index.html', courses = courses, title = title, description = description, price_watch = price_watch, popular_course_all = popular_course_all )

@catalog.route('/<string:url_id>/<int:id>')# Генерируется своя индексная страница категории
def category(url_id,id):	
	model = MsqlCatalog()
	# получаем описание категории	
	category_description = 	model.category_uniq(id)
	# crs_recmmn - получаем из модели рекомендованный курс
	crs_recmmn = category_description['course_recomnd']
	# получаем все курсы данной категории
	courses = model.coursses_id_category(id)
	# получаем описание класса (url_id)
	classes_description = model.classes_uniq_select(url_id)
	# Получаем массив цену и часы удостоверений.
	price_watch = model.price_course_all()
    
	return render_template('catalog/category.html', courses = courses, category_description = category_description, crs_recmmn = crs_recmmn, classes_description = classes_description, price_watch = price_watch  )	

@catalog.route('/course/<int:id>') # выводит один курс
def course(id):  # url_for('catalog.название функции' )
    #подключаем хлебные крошки
	brdcmp = Breadcamp()
    # Получаем модель описания курса
	model = MsqlCatalog()
	course = model.one_course(id)
    # Получаем id класса для подгрузки нужного шаблона 
	category = model.category_uniq(course['id_category'])
	id_classes = category['id_classes']
	# Получаем цену и часы удостоверений.
	price_watch = model.price_course(course['price'])
    # Получаем url образцов удостовирений
	url_certfct = model.certification_jpg(id_classes)
    # Получаем url документа ДПО программы
	doc_pdo = model.doc_pdf(id)
    
	res = request.path
	res = res.split("/")
	# url хлебных крошек для курсов
	breadcamp = brdcmp.course(category, course)
    		
	return render_template('catalog/course.html', course = course, price_watch = price_watch, url_certfct = url_certfct, catalog_url = breadcamp['catalog'], category_url = breadcamp['category'], doc_pdo = doc_pdo  )