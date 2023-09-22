import tkinter as tk

class JuegoTresEnRaya:
    def __init__(self):
        # Inicializar variables de clase
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
        self.tablero = ["", "", "", "", "", "", "", "", ""]
        # Iniciar la interfaz gráfica
        self.iniciar_interfaz()

    def evaluar(self, board, depth):
        # Evaluar el estado actual del tablero
        for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[x] == board[y] == board[z] and board[x] != "":
                return (10 / (1 ** depth) if board[x] == "X" else -10) / (10 ** depth)
        return 0

    def minimax(self, board, depth, maximizing):
        # Implementar algoritmo minimax
        score = self.evaluar(board, depth)
        if score != 0:
            self.puntuacion += score
            return
        if "" not in board:
            return
        for i in range(len(board)):
            if board[i] == "":
                new_board = board.copy()
                new_board[i] = "X" if maximizing else "O"
                self.minimax(new_board, depth + 1, not maximizing)
                if depth == 1:
                    if self.puntuacion < self.mejor_puntuacion:
                        self.mejor_puntuacion = self.puntuacion
                        self.mejor_posicion = new_board
                    self.puntuacion = 0

    def jugar(self, indice):
        # Realizar una jugada
        if self.tablero[indice] == "":
            self.tablero[indice] = "X"
            self.minimax(self.tablero, 1, False)

    def clic_boton(self, indice):
        # Manejar el clic en un botón
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.jugar(indice)
        if self.mejor_posicion is not None:
            self.tablero = self.mejor_posicion
        self.actualizar_botones()

    def actualizar_botones(self):
        # Actualizar el estado de los botones en la interfaz
        for i in range(9):
            self.botones[i].config(text=self.tablero[i])

    def iniciar_interfaz(self):
        # Iniciar la interfaz gráfica con Tkinter
        self.raiz = tk.Tk()
        self.raiz.title("XOXOX")
        self.botones = []
        for i in range(9):
            boton = tk.Button(self.raiz, text="", width=3, bd=3, font=("Roboto Cn", 18), background="silver",
                              command=lambda i=i: self.clic_boton(i))
            boton.grid(row=i // 3 + 1, column=i % 3 + 1)
            self.botones.append(boton)
        self.raiz.mainloop()


if __name__ == "__main__":
    # Iniciar el juego
    juego = JuegoTresEnRaya()


	




	



	


