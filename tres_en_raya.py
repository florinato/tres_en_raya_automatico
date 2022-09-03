global a11
a11=["","","","","","","","",""]
def jugada(a11):

	t=False
	cont=0
	global a12
	a12=["","","","","","","","",""]
	
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
			for v in range (0,9):
				a12[v]=a[v]				
	def max(cont,a):							
		global maxx
		global a12
		if cont>maxx:
			maxx=cont
			for v in range (0,9):
				a12[v]=a[v]		
	def evaluar():
		global eva
		eva=0
		rayas=(0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6)
		rayas_iter=iter(rayas)
		for v in range (0,8):
			i=next(rayas_iter)
			n=next(rayas_iter)
			m=next(rayas_iter)

			if i!="" and a10[i]==a10[n] and a10[i]==a10[m]:
				if a10[i]=="X":
					eva=eva+1
			
				elif a10[i]=="O":
					eva=eva-1
					
		
				
		return(eva)

	i=0
	while i<9:
		
		a1=["","","","","","","","",""]
		
		a1[i]="X"
		a10[i]="X"
		j=0
		
		if a1==a11:
			t=True
			i=9
			

		while j<8:
			
			for v in range (0,9):
				a2[v]=a1[v]
				a10[v]=a1[v]
			p=(-1)
			l=0
			while l<9:
				if a2[l]=="":
					p=p+1
					if p==j:
						a2[l]="O"
						a10[l]="O"
						l=9
				l=l+1
			
			if a11==a10:
				t=True
				i=9
				j=8
				
			n=0
			while n<7:
				for v in range (0,9):
					a3[v]=a2[v]
					a10[v]=a2[v]
				p=(-1)
				l=0
				while l<9:
					if a3[l]=="":
						p=p+1
						if p==n:
							a3[l]="X"
							a10[l]="X"
							l=9
					l=l+1
				if a11==a10:
					t=True
					i=9
					j=8
					n=7
				m=0
				while m<6:
					
					for v in range (0,9):
						a4[v]=a3[v]
						a10[v]=a3[v]
					p=(-1)
					l=0
					while l<9:
						if a4[l]=="":
							p=p+1
							if p==m:
								a4[l]="O"
								a10[l]="O"
								l=9
						l=l+1
					if a11==a10:
						t=True
						i=9
						j=8
						n=7
						m=6
					w=0
					while w<5:
						
						
						for v in range (0,9):
							a5[v]=a4[v]
							a10[v]=a4[v]
						p=(-1)
						l=0
						while l<9:
							if a5[l]=="":
								p=p+1
								if p==w:
									a5[l]="X"
									a10[l]="X"
									l=9
							
							l=l+1
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
							for v in range (0,9):
								a6[v]=a5[v]
								a10[v]=a5[v]
							
							p=(-1)
							l=0
							while l<9:
								if a6[l]=="":
									p=p+1
									if p==f:
										a6[l]="O"
										a10[l]="O"
										l=9
								l=l+1
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
								for v in range (0,9):
									a7[v]=a6[v]
									a10[v]=a6[v]
								p=(-1)
								l=0
								while l<9:
									if a7[l]=="":
										p=p+1
										if p==g:
											a7[l]="X"
											a10[l]="X"
											l=9
									l=l+1
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
									for v in range (0,9):
										a8[v]=a7[v]
										a10[v]=a7[v]
									p=(-1)
									l=0
									while l<9:
										if a8[l]=="":
											p=p+1
											if p==h:
												a8[l]="O"
												a10[l]="O"
												l=9
												
										l=l+1
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
									for v in range (0,9):
										a9[v]=a8[v]
									l=0
									while l<9:
										if a9[l]=="":
											a9[l]="X"
											a10[l]="X"
											l=9
										l=l+1
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
			
					cont=0	 
				n=n+1
			if t==True and a11==a1:
				min(cont,a2)
				cont=0
			
			
					 
			
			j=j+1
		
		
		i=i+1

	return(a12)

	


from tkinter import *
global a
a=["","","","","","","","",""]
def botones(a):
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
def jugar(b):
	global a
	a[b]="X"

	a=jugada(a)
	botones(a)

raiz=Tk()
raiz.title("                        XOXOX")
botones(a)

raiz.mainloop()


	



	


