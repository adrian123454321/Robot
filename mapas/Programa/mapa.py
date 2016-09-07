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


	def quitar_monedas(self):
		for a in (monedas):
			if a=self.x and a=self.y:
				self.monedas.pop(monedas)