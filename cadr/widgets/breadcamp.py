class Breadcamp:
	# ссылка на главную
	home = {'home': 'site.index', }
        # ссылка на каталог
	catalog = {'index': 'catalog.index', 'name': 'Каталог'}		
        
        # формирование ссылки для страницы описание курса
        # входящие атрибуты - модель Категории Курса, модель Курса
	def course(self, category, course):
		href = { 'category': {'index': 'catalog.category' , 'id_url': category['id_url'], 'id': category['id'], 'name':category['name'] }, 'catalog': self.catalog, 'home': self.home }
			
		return   (href)