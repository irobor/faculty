from .. import app,request
from .model import MsqlWidgets
from .form import SearchForm, AskForm # Подключаем форму Поиска, форму заявки



class Widgets(object):
	def __init__(self):
		pass

	@app.context_processor
	def widgetPath():
		a = request.path # получаем полный url
		url_path = a.split("/")
		url_path.pop(0)
		return {'widget_path' : {'url_path': url_path } }	

	@app.context_processor		 
	# КАТАЛОГ здесь мы получаем из БД данные категории. Для Макроса sidebare.  МЕНЮ курсы
	def widgetCatalog():		
		model = MsqlWidgets()
		classes = model.classes_select()	
		category = model.category()			
		return {'widget_catalog': {'classes': classes, 'category': category} }

	@app.context_processor
	# Главное меню навигации НАВИГАЦИЯ
	def widgetMenu():
		form = SearchForm()  # Подключаем форму Поиска
		model = MsqlWidgets()
		menu = model.menu()
		sub_menu = model.sub_menu()
		a = request.path # получаем полный url
		url_active = a.split('/') # разбиваем url на хлебные крошки
		url_active = '/'+url_active[1]+'/'
		return {'widget_menu':{'menu': menu, 'submenu': sub_menu, 'form': form}}

	@app.context_processor
	# Форма для заявки
	def widgetAskForm():
        	form = AskForm() # Подключаем форму Завки
        	return {'widget_formAsk':{'form': form}}

	# УСЛУГИ здесь мы получаем из БД данные услуги для sidbare. МЕНЮ УСЛУГИ
	@app.context_processor
	def widgetService():
		model = MsqlWidgets()		
		sub_menu = model.sub_menu_id_menu(2)
		service_license = model.service_license()
		service_sro = model.service_sro()	
		service_certificates = model.service_certificates()		
		return {'widgetService': {'service_submenu': sub_menu, 'service_license': service_license, 'service_sro': service_sro, 'service_certificates': service_certificates }}

	# Меню для ФУТЕРА
	@app.context_processor
	def widgetFooter():
		model = MsqlWidgets()
		attestation_all = model.attestation()
		sub_menu = model.sub_menu_id_menu(2)
		return{'widget_footer':{'attestation_all': attestation_all, 'sub_menu': sub_menu}	}