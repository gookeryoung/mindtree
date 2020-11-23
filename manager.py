from flask_script import Manager

from app import create_app
from app.index import index
from app.wiki import wiki

app = create_app()
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(wiki, url_prefix='/wiki')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
