from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.config import Config

# Configuración inicial de la ventana
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

class JuegoTresEnRaya(BoxLayout):
    def __init__(self, **kwargs):
        super(JuegoTresEnRaya, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.iniciar_interfaz()
        self.debe_reiniciar = False  # Inicialización de la variable
        self.reiniciar()

    def reiniciar(self):
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
        self.tablero = ["", "", "", "", "", "", "", "", ""]
        self.actualizar_botones()

    def evaluar(self, board, depth):
        for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if board[x] == board[y] == board[z] and board[x] != "":
                return (10 / (1 ** depth) if board[x] == "X" else -10) / (10 ** depth)
        return 0

    def minimax(self, board, depth, maximizing):
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
        if self.tablero[indice] == "":
            self.tablero[indice] = "X"
            self.minimax(self.tablero, 1, False)

    def clic_boton(self, instance):
        if self.debe_reiniciar:
            self.reiniciar()
            self.debe_reiniciar = False
            return
        # Resto del código no modificado...

        if "" not in self.tablero or self.evaluar(self.tablero, 0) != 0:
            self.debe_reiniciar = True
        else:
            self.reiniciar_variables_jugada()

        indice = self.botones.index(instance)
        self.jugar(indice)
        if self.mejor_posicion is not None:
            self.tablero = self.mejor_posicion
        self.actualizar_botones()

        if "" not in self.tablero or self.evaluar(self.tablero, 0) != 0:
            self.debe_reiniciar = True
        else:
            # Reiniciar las variables después de cada jugada
            self.mejor_posicion = None
            self.mejor_puntuacion = 10
            self.puntuacion = 0
    def reiniciar_variables_jugada(self):
        self.mejor_posicion = None
        self.mejor_puntuacion = 10
        self.puntuacion = 0
    def actualizar_botones(self):
        for i in range(9):
            self.botones[i].text = self.tablero[i]

    def iniciar_interfaz(self):
        self.botones = []
        for i in range(3):
            h_layout = BoxLayout()
            for j in range(3):
                boton = Button(font_size=50)
                boton.bind(on_press=self.clic_boton)
                self.botones.append(boton)
                h_layout.add_widget(boton)
            self.add_widget(h_layout)

class TresEnRayaApp(App):
    def build(self):
        return JuegoTresEnRaya()

if __name__ == '__main__':
    TresEnRayaApp().run()
