from flask import Blueprint, render_template, request, send_from_directory, send_file, safe_join

site = Blueprint('site', __name__,template_folder='templates', static_folder='static')

@site.route('/')
def index():
	title = 'Учебный центр Факультет - Курсы повышения квалификации, Профессиональная переподготовка, Рабочие специальности. Сертификат ИСО, Купить Лицензию.'
	description = '''УЦ Факультет предлагает широкий выбор курсов Повышения Квалификации и Профессиональной переподготовки. Освойте Рабочую профессию в короткие сроки. 
	 В Учебном Центре Факультет Вы также можете заказать сертификацию ИСО(ISO) или получить Лицензию. 
	 Дистанционная Форма Дипломы и удостоверения государственного образца. Оформить заявку на обучение можно в центре подготовки кадров по телефону или на сайте.'''
	
	return render_template('site/index.html', title = title, description = description)	

# Маршруты для поисковиков 
@site.route('/robots.txt')
@site.route('/sitemap.xml') 
def static_from_root():
    return send_from_directory(site.static_folder, request.path[1:])
    
"""
string:
int:
float:
path:
uuid:
"""
# Функция скачивания файла Заявки 
@site.route('/download/<string:name>')
def download(name):
	doc = name
	filename = safe_join(site.static_folder, doc) # формируем путь к файлу  и имя файла
	return send_file(filename, download_name = doc, as_attachment=True)    