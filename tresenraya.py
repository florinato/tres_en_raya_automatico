import tkinter as tk

mejor_posicion = None  
mejor_puntuacion =10   
puntuacion=0

# Función para evaluar el estado actual del tablero
def evaluar(board, depth):
    for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]:  # diagonals
        if board[x] == board[y] == board[z] and board[x] != "":
            return (10/ (1 ** depth) if board[x] == "X" else -10) / (10 ** depth)
    return 0

# Función Minimax
def minimax(board, depth, maximizing):
    global mejor_posicion, mejor_puntuacion, puntuacion  # Usar las variables globales
    
    score = evaluar(board, depth)
    if score!=0 :
        puntuacion += score  # Sumar la puntuación a la puntuación total
        return
    if "" not in board:
        
        return

    for i in range(len(board)):
        if board[i] == "":
            new_board = board.copy()
            new_board[i] = "X" if maximizing else "O"
            #print(new_board,puntuacion)
            minimax(new_board, depth + 1, not maximizing)  # Llamada recursiva
            
            if depth == 1:
                #print(mejor_posicion,puntuacion)
                if puntuacion < mejor_puntuacion:
                    mejor_puntuacion = puntuacion
                    mejor_posicion = new_board
                puntuacion =0
               
                    
                
                
def jugar(indice, tablero):
    if tablero[indice] == "":
        tablero[indice] = "X"
        minimax(tablero, 1, False)

# Función para actualizar los botones en la interfaz
def actualizar_botones(tablero):
    for i in range(9):
        botones[i].config(text=tablero[i])

# Función cuando se hace clic en un botón
def clic_boton(indice):
    global tablero, mejor_posicion, mejor_puntuacion
    mejor_posicion = None  # Reiniciar la mejor posición
    mejor_puntuacion = 10  # Reiniciar el mejor puntaje
    
    jugar(indice, tablero)
    
    if mejor_posicion is not None:
        tablero = mejor_posicion
    actualizar_botones(tablero)
tablero = ["", "", "", "", "", "", "", "", ""]
# Inicializar Tkinter
raiz = tk.Tk()
raiz.title("XOXOX")

# Inicializar tablero y botones

botones = []

# Crear los 9 botones y agregarlos a la lista de botones
for i in range(9):
    boton = tk.Button(raiz, text="", width=3, bd=3, font=("Roboto Cn", 18), background="silver", command=lambda i=i: clic_boton(i))
    boton.grid(row=i//3 + 1, column=i % 3 + 1)
    botones.append(boton)

# Iniciar la ventana Tkinter
raiz.mainloop()
	




	



	


