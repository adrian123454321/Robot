def cargar_mapa():
	lista=[]
	p=open("mapa1.txt")
	for l in p:
		print(l)
		lista.append(list(l.strip()))
	print (lista)

def cargar_instrucciones():
	lista=[]
	p=open("programa_1.txt")
	for l in p:
		print(l)
		lista.append(list(l.strip()))
	print (lista)
