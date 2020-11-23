from app.wiki import wiki


@wiki.route('/')
def index():
    return u'这是wiki首页'
