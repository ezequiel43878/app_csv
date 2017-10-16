from flask import Flask 
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
	lista_filas = []
	with open("lista.csv") as archivo:
	
		filas = csv.reader(archivo)
		for fila in filas:
			lista_filas.append(fila)
		
	return render_template('index.html', list = lista_filas )
		
if __name__ == ('__main__'):
	app.run( debug = True, port = 5000)	