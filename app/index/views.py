from app.index import index


@index.route('/')
def index():
    return u'这是index首页'
