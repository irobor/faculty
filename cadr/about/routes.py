from flask import Blueprint, render_template

about = Blueprint('about', __name__, url_prefix='/about', template_folder='templates')



@about.route('/')
def index():
    	# Генерируется своя индексная страница courses	
	title = 'О Компании'			
	return render_template('about/index.html', title = title )