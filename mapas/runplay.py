a=open("mapa1.txt")
for lista in a:
	print(lista)
	lista.append(list(lista.strip()))
print (lista)

def comandos():
	ins=open("programa_1.txt")