#claserobot
#comportamiebtos
	#mover
	#rotar
	#recoger
class Robot(object):
	def __init__(self,x,y,,direccion):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion="UP"
		self.mapa=None

	def mover(self):
		if self.direccion=="UP":
			self.y-=1
		elif self.dereccion=="RIGHT":
			self.x+=1
		elif self.direccion=="DOWN":
			self.y+=1
		else self.x-=1

	def rotar(self):
		if self.direccion=="UP":
			self.direccion="RIGHT"

		elif self.direccion=="RIGHT":
			self.direccion="DOWN"

		elif self.direccion=="DOWN":
			self.direccion="LEFT"

		else self.direccion=="UP":

	def recoger(self):		
		if self.contar_monedas(self.x,self.y)>0:


	def representar(self):
		if self.direccion=="UP":
			return "^"
		elif self.direccion"RIGHT":
			return">"
		elif self.direccion=="DOWN":
			return"v"
		elif self.direccion=="LEFT"