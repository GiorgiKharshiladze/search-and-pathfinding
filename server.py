from bottle import route, run, template, request, static_file
from main import *

@route('/')
def index():
	return template('views/index', list=server_data())

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
	
run(host='localhost', port=8080, debug=True, reloader=True)
