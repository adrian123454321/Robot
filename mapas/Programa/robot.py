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
			self.dereccion="DOWN"

		elif self.direccion=="DOWN":
			self.direccion="LEFT"

		else self.direccion=="UP":

	def recoger(self):
		
		for  in range(len(mapa))


	def representar(self):