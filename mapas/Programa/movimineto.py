import time

map_ancho=40
map_alto=15

def imprimir(x,y):
	result = (" " * map_ancho) * y
	result += " " * x +"*"
	result += " "* map_ancho * (map_alto-(y+1))
	return result

steps=20
for i in range(steps):
	time.sleep(0.4)
	print(imprimir(i,i))