
def jugada(a11):

	t=False # Variable de control para determinar si se ha realizado una jugada.
	cont=0 # Contador de jugadas.
	global a12
	a12=["","","","","","","","",""] # Tablero auxiliar para almacenar jugadas temporales.
	
	a10=["","","","","","","","",""]
	a2=["","","","","","","","",""]
	a3=["","","","","","","","",""]
	a4=["","","","","","","","",""]
	a5=["","","","","","","","",""]
	a6=["","","","","","","","",""]
	a7=["","","","","","","","",""]
	a8=["","","","","","","","",""]
	a9=["","","","","","","","",""]
	
	global eva
	eva=0
	global minn
	global maxx
	maxx=-100 
	minn=100
	def min(cont,a):
		global minn
		global a12
		if cont<minn:
			minn=cont
			a12=copiar(a)			
	def max(cont,a):							
		global maxx
		global a12
		if cont>maxx:
			maxx=cont
			a12=copiar(a)
						
	def evaluar():
		global eva
		eva=0
		rayas=(0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6)
		rayas_iter=iter(rayas)
		for v in range (0,8):
			i=next(rayas_iter)
			n=next(rayas_iter)
			m=next(rayas_iter)

			if a10[i]!="" and a10[i]==a10[n] and a10[i]==a10[m]:
				if a10[i]=="X":
					eva=eva+1
			
				elif a10[i]=="O":
					eva=eva-1
					
		
				
		return(eva)
	def copiar(a):
		aux =["","","","","","","","",""]
		
		for v in range (0,9):
			aux[v]=a[v]
		return aux
	def buscarhueco(a,j,b):
		p=(-1)
		l=0
		while l<9:
			if a[l]=="":
				p=p+1
				if p==j:
					a[l]=b
						
					l=9
			l=l+1
		
		return a
	i=0
	while i<9:
		
		a1=["","","","","","","","",""]
		
		a1[i]="X"
		a10[i]="X"
		
		
		if a1==a11:
			t=True
			i=9
			
		j=0
		while j<8:
			a2=copiar(a1)					
			a2=buscarhueco(a2,j,"O")
			a10=copiar(a2)
			
			if a11==a10:
				t=True
				i=9
				j=8
				
			n=0
			while n<7:
				a3=copiar(a2)
				a3=buscarhueco(a3,n,"X")
				a10=copiar(a3)
			
				
				if a11==a10:
					t=True
					i=9
					j=8
					n=7
				m=0
				while m<6:
					a4=copiar(a3)
					a4=buscarhueco(a4,m,"O")
					a10=copiar(a4)
					
					if a11==a10:
						t=True
						i=9
						j=8
						n=7
						m=6
					w=0
					while w<5:
						a5=copiar(a4)
						a5=buscarhueco(a5,w,"X")
						a10=copiar(a5)
						
						
						
						if a11==a10:
							t=True
							i=9
							j=8
							n=7
							m=6
							w=5
						f=0
						if evaluar()!=0 and t==True:
							cont=cont+eva
							w=5	
							eva=0
							f=4	
							
						
						
						while f<4:
							a6=copiar(a5)
							a6=buscarhueco(a6,f,"O")
							a10=copiar(a6)
							
							
							
							if a11==a10:
								t=True
								i=9
								j=8
								n=7
								m=6
								w=5
								f=4
								
							
							g=0		
							if evaluar()!=0 and t==True:
								cont=cont+eva/10
								f=4
								g=3	
								eva=0
							
							
							while g<3:
								a7=copiar(a6)
								a7=buscarhueco(a7,g,"X")
								a10=copiar(a7)
								
								
								if a11==a10:
									t=True
									i=9
									j=8
									n=7
									m=6
									w=5
									f=4
									g=3
								
								h=0	
								if evaluar()!=0 and t==True:
									cont=cont+eva/100
									g=3
									h=2
									eva=0
								
								while h<2:
									a8=copiar(a7)
									a8=buscarhueco(a8,h,"O")
									a10=copiar(a8)
									
									
									if a11==a10:
										t=True
										i=9
										j=8
										n=7
										m=6
										w=5
										f=4
										g=3
										h=2
									if evaluar()!=0 and t==True:
										cont=cont+eva/1000
										eva=0
										h=2
									a9=copiar(a8)
									buscarhueco(a9,0,"X")
									a10=copiar(a9)
									if a11==a10:
										t=True
										i=9
										j=8
										n=7
										m=6
										w=5
										f=4
										g=3
										h=2	
									if evaluar()!=0 and t==True:
										cont=cont+eva/10000
										eva=0
									if t==True and a11==a8:	
										max(cont,a9)	
										cont=0 		
									if t==True and a11==a7:	
										min(cont,a8)	
										cont=0 
												
									h=h+1
								
								if t==True and a11==a6:	
									max(cont,a7)	
									cont=0 	
								g=g+1
							    
							if t==True and a11==a5:	
								min(cont,a6)	
								cont=0 
									
							f=f+1
						if t==True and a11==a4:	
							max(cont,a5)
							cont=0
						w=w+1
					if t==True and a11==a3:	
						min(cont,a4)
						cont=0 	 
					m=m+1
				if t==True and a11==a2:
					max(cont,a3)	
			
					cont=0 # 	 
				n=n+1
			if t==True and a11==a1:
				min(cont,a2)
				cont=0 
			
			
					 
			
			j=j+1
		
		
		i=i+1

	return(a12)

	


from tkinter import * # Importa el módulo tkinter para la interfaz gráfica.
global a
a=["","","","","","","","",""] # Inicializa el tablero del juego.
def botones(a): # Muestra los botones en la ventana.: # Función que crea y muestra los botones para el juego en la interfaz gráfica.
	boton1=Button(raiz,text=a[0],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(0))
	boton1.grid(row=1,column=1)
	boton2=Button(raiz,text=a[1],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(1))
	boton2.grid(row=1,column=2)
	boton3=Button(raiz,text=a[2],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(2))
	boton3.grid(row=1,column=3)
	boton4=Button(raiz,text=a[3],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(3))
	boton4.grid(row=2,column=1)
	boton5=Button(raiz,text=a[4],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(4))
	boton5.grid(row=2,column=2)
	boton6=Button(raiz,text=a[5],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(5))
	boton6.grid(row=2,column=3)
	boton7=Button(raiz,text=a[6],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(6))
	boton7.grid(row=3,column=1)
	boton8=Button(raiz,text=a[7],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(7))
	boton8.grid(row=3,column=2)
	boton9=Button(raiz,text=a[8],width=3,bd=3,font=("Roboto Cn",18),background="silver",command=lambda: jugar(8))
	boton9.grid(row=3,column=3)
 
def jugar(b): # Función que se llama cuando un jugador realiza una jugada.
	global a
	a[b]="X"
	a=jugada(a)
	botones(a) # actualiza el tablero en la ventana.
	


raiz=Tk() # Crea la ventana principal del juego.
raiz.title("XOXOX") # Establece el título de la ventana.
botones(a) # Muestra los botones en la ventana.
raiz.mainloop() # Inicia el bucle principal de la interfaz gráfica.

	




	



	


