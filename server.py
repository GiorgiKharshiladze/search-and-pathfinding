from bottle import route, run, template, request, static_file
from main import maze_data, mouse_path
import os


start_data = maze_data()
path_data = mouse_path()

@route('/')
def index():
	return template('views/index', start_list=start_data, path_list=path_data)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('static/img/:path#.+#')
def send_static(filename):
    return static_file(filename, root='static/img') 
	
run(host='localhost', port=8080, debug=True, reloader=True)
