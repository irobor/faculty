from flask import Blueprint, render_template
from .. import mysql
from .models import MsqlServices

services = Blueprint('services', __name__, url_prefix='/services', template_folder='templates')
model = MsqlServices()


@services.route('/license')
def license():
    	# Генерируется своя индексная страница courses		
	model = MsqlServices()
	licenses = model.license_all()			
	return render_template('services/license.html', licenses = licenses )

@services.route('/sro')
def sro():
    	# Генерируется своя индексная страница courses
	model = MsqlServices()
	sro = model.sro_all()					
	return render_template('services/sro.html', sro_all = sro )

@services.route('/certificates')
def certificates():
    # Генерируется своя индексная страница все сертификаты
	certificates = model.certificate_all()				
	return render_template('services/certificates.html', certificates = certificates )	

@services.route('/license/<string:name>')
def one_license(name):# Генерируется своя индексная страница одной лицензии		
	license = model.license_one(name)	
	model_doc = model.doc_license('dcm',name)
	model_terms = model.doc_license('terms',name)			
	return render_template('services/license_one.html', license = license, model_doc = model_doc, model_terms = model_terms )		

@services.route('/sro/<string:name>')
def one_sro(name):# Генерируется своя индексная страница одной лицензии	
	sro_one = model.sro_one(name)			
	return render_template('services/sro_one.html', sro_one = sro_one )	

@services.route('/certificate/<string:name>')
def one_certificate(name):# Генерируется своя индексная страница одной лицензии		
	model_cert = model.certificate_one(name)			
	return render_template('services/certificate_one.html', model_cert = model_cert )