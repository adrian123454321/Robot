class Mapa(object):
	def __init__(self,ancho,altura):
		self.ancho=ancho
		self.altura=altura
		self.monedas=[]
		self.robot=None
	def cargar_robot(self,robot):
		self.robot.append(robot)
