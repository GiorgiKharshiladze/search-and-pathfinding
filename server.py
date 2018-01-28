from bottle import route, run, template, request
from main import *

@route('/')
def index():
	mylist = server_data()
	return template('web/index.tpl', list=mylist)
	

run(host='localhost', port=8080, debug=True)