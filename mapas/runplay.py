lista=[]
def cargar_mapa():
	p=open("mapa1.txt")
	for l in p:
		print(l)
		lista.append(list(l.strip()))
	print (lista)


