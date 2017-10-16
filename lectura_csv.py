import csv
lista_filas = []
with open("lista.csv") as archivo:
	
	filas = csv.reader(archivo)
	for fila in filas:
		lista_filas.append(fila)

for fila in lista_filas:
	print ("<tr>")
	for columna in fila:
		print ("<td>"+columna+"</td>")
	print("</tr>")	


		