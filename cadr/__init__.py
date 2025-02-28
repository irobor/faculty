from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL # Подключаем батарейку для работы с Mysql


    
mysql = MySQL()
sqlalchm = SQLAlchemy()

def create_app():    
    app = Flask(__name__)
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'
    app.config.from_pyfile('setting.py') #подгружаем настройки БД

    mysql.init_app(app) # Для работы с БД Mysql
    sqlalchm.init_app(app) # Для работы с БД
    
    
 
    
    from .site.routes import site
    from .attestation.routes import attestation
    from .catalog.routes import catalog
    from .services.routes import services
    from .contacts.routes import contacts
    from .about.routes import about
    from .search.routes import search
    from .ask.routes import ask
    
    app.register_blueprint(site)
    app.register_blueprint(attestation)
    app.register_blueprint(catalog)
    app.register_blueprint(services)
    app.register_blueprint(contacts)
    app.register_blueprint(about)
    app.register_blueprint(search)
    app.register_blueprint(ask)
    
    
    return app

app = create_app()

from .widgets import widget # подключаем виджеты для макросов
from .error import errors # Обработчик исключений 404, 500

    # Start development web server
if __name__ == '__main__':
    app = create_app()
#    app.run(host='0.0.0.0', port=5000, debug=True)
