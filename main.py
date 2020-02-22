#rosputny_v

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
	name = request.args.get("name", "World")
	return f'Rosputnii Valentyn TZ-72'

@app.route('/first')
def helllo():
	a = None
	b = 123
	c = 'fghjk'
	return f'{a}, {b}, {c}'

if __name__ == '__main__':
	app.run('0.0.0.0')
