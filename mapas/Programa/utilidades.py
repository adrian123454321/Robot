def cargar_mapa():
	lista=[]
	p=open("programa/mapa1.txt")
	for l in p:
		print(l)
		lista.append(list(l.strip()))
	print (lista)
#lista de listas 
def cargar_instrucciones():
	lista=[]
	p=open("programa/programa_1.txt")
	for l in p:
		print(l)
		lista.append(list(l.strip()))
	print (lista)
