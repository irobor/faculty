from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__, url_prefix='/contacts', template_folder='templates')



@contacts.route('/')
def index():
    	# Генерируется своя индексная страница courses	
	echo = 'здесь будет страница с Контактами Компании'			
	return render_template('contacts/index.html', echo = echo )