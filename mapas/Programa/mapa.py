class Mapa(object):
	def __init__(self,ancho,altura):
		self.ancho=ancho
		self.altura=altura
		self.monedas=[]
		self.robot=None
	def cargar_robot(self,robot):
		self.robot.append(robot)

	def agregar_monedas(self,monedas):
		self.monedas.append(monedas)

	def contar_monedas(self):
		contador=0
		for monedas in self.monedas:
			if moneda.x==x and moneda.y=y:
				contador+=1
 
	def quitar_monedas(self):
		for a in (monedas):
			if a=self.x and a=self.y:
				self.monedas.pop(monedas)

	