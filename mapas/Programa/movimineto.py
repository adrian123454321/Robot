import time

mao_ancho=70
map_alto=19

def imprimit(x,Y):
	result = (" " * map_ancho) * Y
	result += " " * X +"*"
	result += " "* map_ancho * (map_alto-(y+1))
	return result

steps=20
for i in range(steps):
	time.sleep(0.4)
	print(imprimir(i,i))