from flask import Blueprint, render_template,request
from .models import MsqlSearch
from ..widgets.form import SearchForm #подключаем форму поиска
from ..catalog.models import MsqlCatalog #подключаем модель из catalog, запрос для прайса

search = Blueprint('search', __name__, url_prefix='/search', template_folder='templates')

# оброботчик формы поиска
@search.route('/', methods = ['GET', 'POST'])
def index(): 
    title = 'Поиск в нашем каталоге'
    form = SearchForm()   # Класс оброботчика формы  
    model_catalog = MsqlCatalog() # модель Catalog
    model = MsqlSearch()    # Класс модели БД
    if form.validate_on_submit():  # собирает все данные, запускает все валидаторы, прикрепленные к полям, и если все в порядке, вернет True            
        queryForm = form.searched.data  # все данные из формы поиска
        count = 0
        l = len(queryForm)
        post = queryForm
        for number in range(3,l):
            if not model.search_courses(post):#запрос модель
                count +=1
                post = post[:l -count]
        
        price_watch = model_catalog.price_course_all()	# Получаем массив цену и часы удостоверений.
        result = model.search_courses(post)#запрос модель 
        lnArray = len(result)  # кол-во элементом в массиве      
        return render_template('search/result.html', title = title, result = result, ln = lnArray, queryForm = queryForm, price_watch = price_watch)        
    else:
        return render_template('search/search.html', title = title, form = form, no = 'Нет данных')    