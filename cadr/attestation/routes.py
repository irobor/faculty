from flask import Blueprint, render_template
from .models import MsqlAttestation


attestation = Blueprint('attestation', __name__, url_prefix='/attestation', template_folder='templates')


@attestation.route('/')
def index():
    	# Генерируется своя индексная страница все аттестации 
    model = MsqlAttestation()
    attest = model.attest_all()
    title = 'Аттестация инженерно-технических работников (ИТР)'
    description = """После успешного прохождения аттестации инженерно-технический работник получает удостоверение ИТР.
                    Что даст аттестация ИТР организации. Удостоверение ИТР, а также протоколы аттестации могут быть 
                    затребованы при проверке или при несчастных случаях. Документ, подтверждающий квалификацию ИТР,
                    в частности, позволяет организации получить допуск СРО,
                    который даёт возможность вести работы и оказывать услуги в строительном секторе."""
    return render_template('attestation/index.html', title = title, attest = attest )

# Странца одной аттестации 
@attestation.route('/<string:url_id>')
def attestation_one(url_id):
    model = MsqlAttestation()
    attest = model.attest_one(url_id)
    table = model.attest_table(attest['id'])# получаем id аттесстации
    ulr_doc = model.download_file(url_id) # url для скачивания документа (Заявка)
    img_url = model.img_certificat(url_id) # url для img (образец удостоверения )
    return render_template('attestation/attestation_one.html', attest = attest, table = table, ulr_doc = ulr_doc, img_url = img_url )