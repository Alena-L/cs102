from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def index(name="Pretty :3"):
    return template('<em>Hello {{name}}</em>!', name=name)

run(host='localhost', port=8080)
