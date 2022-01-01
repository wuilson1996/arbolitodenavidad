from tkinter import *
import tkinter.font as tkFont
import random
from pygame import mixer

# Clase
class Arbolito():
	# Se inicializa variables
	def __init__(self):
		self.colores=["#97FF00","#FF3A00","#FF9E00","#FFEC00","#80FF00","#04FF00","#0000FF","#C900FF","#FF0051","#FF001F","#FF7800","#FF9E00"]
		self.ventana=Tk()
		self.ventana.geometry("800x700")
		self.ventana.configure(bg="black")
		self.x=400
		self.y=40
		self.i=1
		self.Luz=[]
		self.navidad=Label(self.ventana,text="Feliz Navidad 2021 y Prospero año Nuevo")
		self.llenar()
		self.ventana.mainloop()

	# Inicia el arbolito
	def llenar(self,aux=0):
		for i in range(self.i):

			self.luz=Label(self.ventana,text="*",font=tkFont.Font(size=20),fg="white",bg="black")
			self.luz.place(x=self.x-(i*20),y=self.y)

		if(aux==3):
			
			self.x-=20*2
			self.i-=4
			self.ventana.after_cancel(self.acum)
			self.acum=self.ventana.after(100,self.llenar,aux-3)
		
		elif(self.x<=720):
			if(aux==2):

				self.x+=20*2
				self.y+=20
				self.i+=4
				self.ventana.after_cancel(self.acum)
				self.acum=self.ventana.after(100,self.llenar,(aux+1))

			else:

				self.x+=20
				self.y+=20
				self.i+=2
				self.acum=self.ventana.after(100,self.llenar,(aux+1))
		else:

			self.ventana.after_cancel(self.acum)
			self.x=340
			self.y+=20
			for i in range(4):
				for j in range(7):

					self.pie=Label(self.ventana,text="*",font=tkFont.Font(size=20),fg="white",bg="black")
					self.pie.place(x=self.x+(j*20),y=self.y)
				
				self.y+=20

			self.y=20
			self.x=400
			self.Musica()
			self.animar()

	# Generar animacion de colores
	def animar(self,aux=0):

		if(aux>=1):
			j=40
			self.y=100
			for i in range(1,9,1):
			
				Label(self.ventana,text="*",font=tkFont.Font(size=25),fg=random.choice(self.colores),bg="black").place(x=self.x+(j+60), y=self.y)
				Label(self.ventana,text="*",font=tkFont.Font(size=25),fg=random.choice(self.colores),bg="black").place(x=self.x-(j+60), y=self.y)
				j+=40
				self.y+=60

			self.y=20
			self.x=400
			self.ventana.after_cancel(self.acum)
			self.acum=self.ventana.after(500,self.animar,aux-1)

		else:
			Label(self.ventana,text="*",font=tkFont.Font(size=25),fg=random.choice(self.colores),bg="black").place(x=self.x, y=self.y-10)
			self.navidad.configure(font=tkFont.Font(size=30),fg=random.choice(self.colores),bg="black")
			self.navidad.place(x=25, y=650)
			self.acum=self.ventana.after(500,self.animar,aux+1)
	# Sonido
	def Musica(self):
		
		mixer.init()
		mixer.music.load('sonido.mp3')
		mixer.music.play()

if __name__ == "__main__":
	arbol=Arbolito()