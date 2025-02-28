from flask import Blueprint, render_template, url_for, redirect
from ..widgets.form import AskForm #подключаем форму Заявки
import requests

ask = Blueprint('ask', __name__, url_prefix='/ask', template_folder='templates')


@ask.route('/', methods = ['GET', 'POST'])
def index():
    form = AskForm()   # Класс оброботчика формы 
    name = ''
    phone = None
    textArea = ''

    token = ""
    url = "https://api.telegram.org/bot"
    channel_id = ""
    url += token
    method = url + "/sendMessage"
    
    if form.validate_on_submit(): # собирает все данные, запускает все валидаторы, прикрепленные к полям, и если все в порядке, вернет True  
        name = form.name.data  # все данные из формы поиска
        form.name.data = '' #сбрасываем
        phone = form.phone.data
        form.phone.data = '' #сбрасываем
        textArea = form.textArea.data
        form.textArea.data = '' #сбрасываем
        text = name + "\n" + phone + "\n" + textArea
        r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text 
          })
        return render_template('ask/index.html')          
    else:
        return redirect(url_for('catalog.index'), 301) 


    

    

    